# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import peer, hashTable, refTable
# from channels.auth import channel_session_user
import datetime

class showDatabaseConsumer(WebsocketConsumer):

    # @channel_session_user
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.client = self.scope['client']
        
        print(self.client[0])
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        peerid, active = peer.objects.get_or_create(peer_ip=self.client[0], active=False) 
        print(peer.objects.all())   
        self.accept()


    def disconnect(self, close_code):
        # Leave room group
        peer_inactive = peer.objects.get(peer_ip=self.client[0])
        peer_inactive.active = False
        peer_inactive.save()

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        query = text_data_json['query']
        filehash = text_data_json['hash']

        if query == 'Search':
            response = refTable.objects.filter(filehash=filehash)
            save_table = hashTable.objects.filter(filehash=filehash).update(lastuseddate=datetime.date.today)
            save_table.save()

        elif query == 'Share':
            size = text_data_json['size']
            '''
            Fill this
            '''

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'response',
                'response': response
            }
        )
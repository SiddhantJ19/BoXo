# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
import json
from .models import peer, hashTable, refTable
import datetime

class showDatabaseConsumer(JsonWebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)('active',self.channel_name)
        self.accept() 
        

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'active',
            self.channel_name
        )

    # Receive message from WebSocket
    def receive_json(self, content):

        '''
            Message= {
            'command': Share/Unshare/Search
            'hash' : filehash -Share/unshare
            'size' : filesize  -share
            'Filename':filename -search/share/unshare
            }
            -->>Share
            self.client = self.scope['client'] --> store in database
            Shareddate - scope
            lastuseddate - same
        '''
        command = content.get("command", None)
        if command =='Share':
            print(content)
            print("debug111")
            peerid = self.scope['client'][0]
            shareddate = datetime.date.today
            lastuseddate = datetime.date.today  
            file_obj, file_obj_created  =  hashTable.objects.get_or_create(filename=content['filename'],
                                                                            filehash=content['hash'], 
                                                                             size=content['size'], 
                                                                             defaults={'shareddate': shareddate,
                                                                                        'lastuseddate':lastuseddate})
            print("debug")
            file_obj.save()

            peer_obj, peer_obj_created = peer.objects.get_or_create(peer_ip=peerid)
            peer_obj.save()

            refTableobj, refTableobj_created = refTable.objects.get_or_create(peer=peer_obj, filehash=file_obj)
            refTableobj.save()

            self.send_json({
                "message" : "Stored in database"
                })

        elif command == 'Unshare':
            pass
        
        elif command == 'Search':
            filename = content['filename']
            get_fileinfo =  hashTable.objects.filter(filename__contains=filename).values('filename','filehash','size')
            print(get_fileinfo.query)
            get_peerinfo = refTable.objects.filter(filehash__filehash__in=[file['filehash'] for file in get_fileinfo]).values('filehash__filehash','filehash__size','peer__peer_ip')
            print(list(get_peerinfo))
            self.send_json({ 
                "Peer_List" : list(get_peerinfo),
                })



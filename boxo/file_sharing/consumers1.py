from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from models1 import fileorFolder, peer

class Tracker(AsyncJsonWebsocketConsumer):
	
	"""
    This consumer handles websocket connections for clients.

    It uses AsyncJsonWebsocketConsumer, which means all the handling functions
    must be async functions, and any sync work (like ORM access) has to be
    behind database_sync_to_async or sync_to_async. For more, read
    http://channels.readthedocs.io/en/latest/topics/consumers.html
    """
	
	##### WebSocket event handlers
	async def connect(self):
		"""
		Called when the websocket is handshaking as part of initial connection.
		"""
		await self.accept()


	async def disconnect(self):
		# await self.close()
		pass

	async def recieve_json(self, content):
	    """
	    Called when we get a text frame. Channels will JSON-decode the payload
	    for us and pass it as the first argument.
	    """
	    # Messages will have a "command" key we can switch on
		command = content.get('command', None)
		try:
			if command == 'Search':
				fileInfo = await Search(content['FileName'])
				if fileInfo

			elif command == 'Share':
				fileInfo = await Share(content)
				if fileInfo:
					self.send_json({'list':fileInfo})
					# To be Continued

			elif command == 'UnShare':
				pass

		except Exception as e:
			raise e


	@database_sync_to_async		
	def Search(FileName):
		try:
			# .values() creates an instance of a list i.e 
			#[{'filename':val1, 'filehash': val2}{'filename':val3, 'filehash': val4}]
			return fileorFolder.objects.filter(file_name__contains=FileName).values()

		except Exception as e:
			raise e

		'''
		This function recieves query_type variable and does corresponding tasks.
		query_type = [Share, Search, Unshare]
		Write Exceptions
		''' 
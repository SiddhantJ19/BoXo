from django.db import models

class fileorFolder(models.Model):
	"""
	only for files for now
	"""
	file_name = models.CharField(max_length=100)
	file_hash = models.CharField(max_length=100, primary_key =True)
	number_peers = models.IntegerField()

class peer(models.Model):
	file_hash = models.ForiegnKey(fileorFolder, on_delete=models.CASCADE)
	peer = models.CharField(max_length=16)



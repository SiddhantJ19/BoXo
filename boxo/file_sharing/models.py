from django.db import models
import datetime

class peer(models.Model):		
	peer_ip = models.CharField(max_length=16, primary_key=True)
	Ratings = models.IntegerField(null=True)
	# lastactive = models.DateField(default=datetime.date.today)
	active = models.BooleanField(default=False)


class hashTable(models.Model):
	filehash =  models.CharField(unique=True, max_length=50)
	shareddate = models.DateField(default=datetime.date.today)
	lastuseddate = models.DateField(default=datetime.date.today)
	size = models.IntegerField(null=False)
	delete_flag = models.BooleanField(default=False)
	downloads = models.IntegerField(default=0)
	peer_id = models.ManyToManyField(peer, through="refTable")


class refTable(models.Model):
	peer = models.ForeignKey(peer, on_delete=models.CASCADE)
	filehash = models.ForeignKey(hashTable, on_delete=models.CASCADE)
	downloadswithpeer = models.IntegerField()
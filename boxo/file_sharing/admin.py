from django.contrib import admin
from .models import peer, hashTable, refTable
# Register your models here.

admin.site.register(peer)
admin.site.register(hashTable)
admin.site.register(refTable)
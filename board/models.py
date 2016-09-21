from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import hashers
# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank=False)
    created_date = models.DateField(auto_now_add=True)
    contents = models.TextField(blank=False)
    hits = models.IntegerField(default=0, blank=False)

    def get_absolute_url(self):
        return reverse('board_view', args=(self.id,1))
    
    def get_replys(self):
        return Reply.objects.filter(board_id=self.id)

class Reply(models.Model):
    id = models.AutoField(primary_key=True)
    board = models.ForeignKey(Board, default=None)
    depth_id = models.PositiveSmallIntegerField()
    reply = models.TextField(blank=False)
    name = models.TextField(blank=False)
    password = models.CharField(max_length=256)
    ipaddress = models.CharField(max_length=20, blank=False)
    created_date = models.DateField(auto_now_add=True)
    
    def save(self):
        self.password = hashers.make_password(self.password)
        # print("save", self.password)
        return super().save()

    

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import hashers
from itertools import chain
# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    contents = models.TextField(blank=False)
    hits = models.IntegerField(default=0, blank=False)

    def get_absolute_url(self):
        return reverse('board_view', kwargs={"board_id":self.id})

    def get_replys(self):
        # reply_withchild = Reply.objects.none()
        reply_withchild = []
        depth = 0
        replys = Reply.objects.filter(board=self, depth=depth)
        depth += 1
        for reply in replys:
            # reply_withchild = chain(reply_withchild, reply, reply.get_reply_child(self))
            reply_withchild.append(reply)
            reply_withchild.extend(list(reply.get_reply_child(self)))
            # print(reply_withchild)
            # chain(reply_withchild, )
        return reply_withchild

    def get_replys_count(self):
        return Reply.objects.filter(board_id=self.id).count()

class Reply(models.Model):
    id = models.AutoField(primary_key=True)
    board = models.ForeignKey(Board, default=None)
    parent = models.ForeignKey("self", default=None, null=True, blank=True)
    depth = models.PositiveSmallIntegerField(default=0)
    comment = models.TextField(blank=False)
    name = models.TextField(blank=False)
    password = models.CharField(max_length=256)
    ipaddress = models.CharField(max_length=20, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def save(self):
        self.password = hashers.make_password(self.password)
        # print("save", self.password)
        return super().save()

    def get_reply_child(self, board):
        # child = Reply.objects.none()
        child = []
        replys = Reply.objects.filter(board=board, parent=self)
        for reply in replys:
            child.append(reply)
            child.extend(list(reply.get_reply_child(board)))
            # child = chain(child, reply, reply.get_reply_child(board))
            # chain(child, )
        return child

    

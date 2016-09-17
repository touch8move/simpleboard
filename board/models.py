from django.db import models
from django.core.urlresolvers import reverse
import logging
# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank=False)
    created_date = models.DateField(auto_now_add=True)
    # mail = models.CharField(max_length=50)
    contents = models.TextField(blank=False)
    hits = models.IntegerField(default=0, blank=False)

    def get_absolute_url(self):
        return reverse('board_view', args=(self.id,1))

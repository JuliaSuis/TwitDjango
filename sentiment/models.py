#from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

#class ResultsText(models.Model):
#    text = models.TextField()

class Query(models.Model):
    tag = models.TextField()

def save_query(self):
    self.save()

def __str__(self):
    return self.tag



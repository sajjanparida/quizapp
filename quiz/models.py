# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
    question=models.ImageField(upload_to='quiz/img')
    answer=models.TextField()
    name=models.CharField(max_length=100,default='your name')
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    disappear=models.BooleanField(default=False)
    again=models.BooleanField(default=False)
    def __unicode__(self):
			return self.name 


class User(models.Model):
    name=models.CharField(max_length=60)
    username=models.CharField(max_length=80)
    score=models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name

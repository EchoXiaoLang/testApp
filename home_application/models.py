# -*- coding: utf-8 -*-
from django.db import models

class Tb_Work(models.Model):
    name = models.CharField(max_length=32,null=True)
    position = models.CharField(max_length=32,null=True)
    sex = models.CharField(max_length=32,null=True)
    age = models.CharField(max_length=32,null=True)
    origo = models.EmailField(max_length=32,null=True)
    phone = models.CharField(max_length=32,null=True)
    updatetime = models.DateTimeField(auto_now=True)
    emial = models.EmailField(max_length=32,null=True)
    note = models.CharField(max_length=32,null=True)

    def __unicode__(self):
        return self.title
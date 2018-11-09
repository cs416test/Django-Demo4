# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.`>

class People(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField()
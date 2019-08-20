# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Request(models.Model):
	name = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)

	class Meta:
		db_table = "request"

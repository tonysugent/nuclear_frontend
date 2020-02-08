# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models


class Countries(models.Model):
    country = models.CharField(max_length=25,null=True)
    reactors = models.CharField(max_length=25,null=True)
    capacity_total = models.FloatField(null=True)
    generated_electricity = models.FloatField(null=True)
    percent_use = models.FloatField(null=True)
    country_code = models.CharField(max_length=3,null=True)


class Reactors(models.Model):
    country_id = models.IntegerField(null=True)
    name = models.CharField(max_length=25, null=True)
    type = models.CharField(max_length=25, null=True)
    status = models.CharField(max_length=25, null=True)
    city = models.CharField(max_length=25, null=True)
    rup = models.IntegerField(null=True)
    gec = models.IntegerField(null=True)
    fgc = models.IntegerField(null=True)

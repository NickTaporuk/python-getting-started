from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone


class Apartment(models.Model):
    countryId = models.IntegerField(null=False)
    typeSettlementId = models.IntegerField(null=False)
    settlementId = models.IntegerField(null=False)
    districtId = models.IntegerField(null=False)
    streetId = models.IntegerField(null=False)
    houseNumber = models.IntegerField(null=False)
    apartmentNumber = models.IntegerField(null=True)
    imagesId = models.IntegerField(null=True)
    zipId = models.IntegerField(null=True)
    detailsInfoJson = JSONField()
    publishedDate = models.DateTimeField(default=timezone.now())
    updatedDate = models.DateTimeField(default=timezone.now())




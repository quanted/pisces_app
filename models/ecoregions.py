from django.db import models

class EcoRegions(models.Model):
    """Model class for Eco Regions"""
    pk_uid = models.IntegerField(primary_key=True)
    aggregated = models.TextField(max_length=50)

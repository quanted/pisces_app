from django.db import models

class EcoRegions(models.Model):
    """Model class for Eco Regions"""
    gid = models.IntegerField(primary_key=True)
    aggregated = models.TextField(max_length=50)
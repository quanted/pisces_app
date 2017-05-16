from django.db import models

class FishGenusProperties(models.Model):
    """Model class for Fish Genus Properties"""

    CommonName = models.TextField(max_length=50, primary_key=True)
    Genus = models.TextField(max_length=25)
    Species = models.TextField(max_length=25)
    Max_Size = models.FloatField
    HUC = models.TextField(max_length=8)
    GenusID = models.IntegerField
    Cond_L = models.FloatField
    Cond_U = models.FloatField
    pH_L = models.FloatField
    pH_U = models.FloatField
    Width_L = models.FloatField
    Width_U = models.FloatField
    Slope_L = models.FloatField
    Slope_U = models.FloatField
    Area_L = models.FloatField
    Area_U = models.FloatField
    Depth_L = models.FloatField
    Depth_U = models.FloatField
    DO_L = models.FloatField
    DO_U = models.FloatField
    TSS_L = models.FloatField
    TSS_U = models.FloatField
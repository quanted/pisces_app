from django.db import models

class NHDAttributes(models.Model):
    """Model class for Fish Genus Properties"""

    comid = models.IntegerField
    totdasqkm = models.FloatField
    maxelevsmo = models.FloatField
    minelevsmo = models.FloatField
    slope = models.FloatField
    precipvc = models.FloatField
    maflowv = models.FloatField
    mavelv = models.FloatField
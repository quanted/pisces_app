from django.db import models

class EcoRegions(models.Model):
    """Model class for Eco Regions"""
    gid = models.IntegerField(db_column='gid', primary_key=True)
    aggregated = models.TextField(max_length=50)

    def get_attributes(self):
        attrib = dict()
        attrib['gid'] = self.gid
        attrib['aggregated'] = self.aggregated

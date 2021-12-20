from django.db import models

class Hucs(models.Model):
    """Model class for huc8s"""

    speciesid = models.IntegerField(db_column='speciesid', primary_key=True)
    huc = models.TextField( max_length=8)

    def get_attributes(self):
        attrib = dict()
        attrib['speciesid'] = self.speciesid
        attrib['huc'] = self.huc
        return attrib
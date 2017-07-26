from django.db import models

class FishNames(models.Model):
    """Model class for fish name properties"""

    speciesid = models.IntegerField(db_column='speciesid', primary_key=True)
    commonname = models.TextField( max_length=50)
    species = models.TextField(max_length=25)

    def get_attributes(self):
        attrib = dict()
        attrib['speciesid'] = self.speciesid
        attrib['common_name'] = self.commonname
        attrib['scientific_name']= self.species
        return attrib
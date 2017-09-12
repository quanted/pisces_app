from django.db import models

class Segments(models.Model):
    """This class is a wrapper for a NHD+ Flowline Segment - maps to a Segment node"""

    def __init__(self):
        self.comid = models.IntegerField(db_column='comid', primary_key=True)
        self.totdasqkm = models.FloatField
        self.maxelevsmo = models.FloatField
        self.minelevsmo = models.FloatField
        self.slope = models.FloatField
        self.precipvc = models.FloatField
        self.maflowv = models.FloatField
        self.mavelv = models.FloatField

    def get_attributes(self):
        attrib = dict()
        attrib['comid'] = self.comid
        attrib['totdasqkm'] = self.totdasqkm
        attrib['maxelevsmo']= self.maxelevsmo
        attrib['minelevsmo'] = self.minelevsmo
        attrib['slope'] = self.slope
        attrib['precipvc'] = self.precipvc
        attrib['maflowv'] = self.maflowv
        attrib['mavelv'] = self.mavelv
        return attrib
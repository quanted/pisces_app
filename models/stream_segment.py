from django.db import models

class Segments(models.Model):
    """This class is a wrapper for a NHD+ Flowline Segment - maps to a Segment node"""
    comid = models.IntegerField(db_column='comid', primary_key=True)
    totdasqkm = models.FloatField
    maxelevsmo = models.FloatField
    minelevsmo = models.FloatField
    slope = models.FloatField
    precipvc = models.FloatField
    maflowv = models.FloatField
    mavelv = models.FloatField

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
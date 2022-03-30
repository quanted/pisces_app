from django.db import models

class FishGenusProperties(models.Model):
    """Model class for Fish Genus Properties"""

    speciesid = models.IntegerField(db_column='speciesid', primary_key=True)
    commonname = models.TextField( max_length=50)
    genus = models.TextField(max_length=25)
    species = models.TextField(max_length=25)
    mean_weight = models.FloatField
    thinning = models.FloatField
    thin_adj = models.FloatField
    rarity = models.FloatField
    huc = models.TextField(max_length=8)
    #speciesid = models.IntegerField
    genusid = models.IntegerField
    cond_l = models.FloatField
    cond_u = models.FloatField
    ph_l = models.FloatField
    ph_u = models.FloatField
    width_l = models.FloatField
    width_u = models.FloatField
    slope_l = models.FloatField
    slope_u = models.FloatField
    area_l = models.FloatField
    area_u = models.FloatField
    depth_l = models.FloatField
    depth_u = models.FloatField
    do_l = models.FloatField
    do_u = models.FloatField
    tss_l = models.FloatField
    tss_u = models.FloatField

    def get_attributes(self):
        attrib = dict()
        attrib['species_id'] = self.speciesid
        attrib['common_name'] = self.commonname
        attrib['genus'] = self.genus
        attrib['species']= self.species
        attrib['mean_weight'] = self.mean_weight
        attrib['thinning'] = self.thinning
        attrib['thin_adj'] = self.thin_adj
        attrib['rarity'] = self.rarity
        attrib['huc'] = self.huc
        attrib['genusID'] = self.genusid
        attrib['cond_l'] = self.cond_l
        attrib['cond_u'] = self.cond_u
        attrib['ph_l'] = self.ph_l
        attrib['ph_u'] = self.ph_u
        attrib['width_l'] = self.width_l
        attrib['width_u'] = self.width_u
        attrib['slope_l'] = self.slope_l
        attrib['slope_u'] = self.slope_u
        attrib['area_l'] = self.area_l
        attrib['area_u'] = self.area_u
        attrib['depth_l'] = self.depth_l
        attrib['depth_u'] = self.depth_u
        attrib['do_l'] = self.do_l
        attrib['do_u'] = self.do_u
        attrib['tss_l'] = self.tss_l
        attrib['tss_u'] = self.tss_u
        return attrib


class FishGenusPropertiesV2(models.Model):
    """Model class for Fish Genus Properties"""

    speciesid = models.IntegerField(db_column='speciesid', primary_key=True)
    commonname = models.TextField( max_length=50)
    genus = models.TextField(max_length=25)
    species = models.TextField(max_length=25)
    mean_weight = models.FloatField
    thinning = models.FloatField
    thin_adj = models.FloatField
    rarity = models.FloatField
    huc = models.TextField(max_length=8)
    #speciesid = models.IntegerField
    genusid = models.IntegerField
    slope_l = models.FloatField
    slope_u = models.FloatField
    area_l = models.FloatField
    area_u = models.FloatField
    elev_l = models.FloatField
    elev_u = models.FloatField
    iwi_l = models.FloatField
    iwi_u = models.FloatField
    bmmi_l = models.FloatField
    bmmi_u = models.FloatField
    model = models.IntegerField
    crit_p0 = models.FloatField
    crit_p1 = models.FloatField
    crit_ave = models.FloatField
    crit_1sd = models.FloatField
    crit_2sd = models.FloatField

    def get_attributes(self):
        attrib = dict()
        attrib['species_id'] = self.speciesid
        attrib['common_name'] = self.commonname
        attrib['genus'] = self.genus
        attrib['species']= self.species
        attrib['mean_weight'] = self.mean_weight
        attrib['thinning'] = self.thinning
        attrib['thin_adj'] = self.thin_adj
        attrib['rarity'] = self.rarity
        attrib['huc'] = self.huc
        attrib['genusID'] = self.genusid
        attrib['slope_l'] = self.slope_l
        attrib['slope_u'] = self.slope_u
        attrib['area_l'] = self.area_l
        attrib['area_u'] = self.area_u
        attrib['elev_l'] = self.elev_l
        attrib['elev_u'] = self.elev_u
        attrib['iwi_l'] = self.iwi_l
        attrib['iwi_u'] = self.iwi_u
        attrib['bmmi_l'] = self.bmmi_l
        attrib['bmmi_u'] = self.bmmi_u
        attrib['model'] = self.model
        attrib['crit_p0'] = round(100 * self.crit_p0, 2) if not None else 0.0
        attrib['crit_p1'] = round(100 * self.crit_p1, 2) if not None else 0.0
        attrib['crit_ave'] = round(100 * self.crit_ave) if not None else 0.0
        attrib['crit_1sd'] = round(100 * self.crit_1sd) if not None else 0.0
        attrib['crit_2sd'] = round(100 * self.crit_2sd) if not None else 0.0
        return attrib


class FishGenusPropertiesV3(models.Model):
    """Model class for Fish EnvelopesV3"""
    speciesid = models.IntegerField(db_column='speciesid', primary_key=True)
    modelid = models.IntegerField
    slope_l = models.FloatField
    slope_u = models.FloatField
    elev_l = models.FloatField
    elev_u = models.FloatField
    iwi_l = models.FloatField
    iwi_u = models.FloatField
    bmmi_l = models.FloatField
    bmmi_u = models.FloatField
    wa_l = models.IntegerField
    wa_u = models.FloatField

    def get_attributes(self):
        attrib = dict()
        attrib['species_id'] = self.speciesid
        attrib['modelid'] = self.modelid
        attrib['slope_l'] = self.slope_l
        attrib['slope_u'] = self.slope_u
        attrib['wa_l'] = self.wa_l
        attrib['wa_u'] = self.wa_u
        attrib['elev_l'] = self.elev_l
        attrib['elev_u'] = self.elev_u
        attrib['iwi_l'] = self.iwi_l
        attrib['iwi_u'] = self.iwi_u
        attrib['bmmi_l'] = self.bmmi_l
        attrib['bmmi_u'] = self.bmmi_u
        return attrib

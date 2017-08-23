from django.db import models

class FishSpeciesProperties(models.Model):
    """Model class for Fish Species Properties"""

    speciesid = models.IntegerField(db_column='speciesid', primary_key=True)
    genusid = models.IntegerField
    genus = models.TextField(max_length=25)
    species = models.TextField(max_length=25)
    commonname = models.TextField(max_length=50)
    family = commonname = models.TextField(max_length=50)
    grp = models.TextField(max_length=50)
    native = models.CharField
    pfg_page = models.IntegerField
    sportfishing = models.TextField(max_length=1)
    nongame = models.TextField(max_length=1)
    subsis_fish = models.TextField(max_length=1)
    pollut_tol = models.TextField(max_length=100)
    max_length = models.FloatField
    mean_length = models.FloatField
    mean_weight = models.FloatField
    thinning = models.FloatField
    thin_adj = models.FloatField
    max_age = models.IntegerField
    w_l_a = models.FloatField
    w_l_b = models.FloatField
    l_w_c = models.FloatField
    l_w_d = models.FloatField
    regress = models.TextField(max_length=1)
    rarity = models.IntegerField
    caves = models.TextField(max_length=10)
    springs = models.TextField(max_length=10)
    headwaters = models.TextField(max_length=10)
    creeks = models.TextField(max_length=10)
    small_riv = models.TextField(max_length=10)
    med_riv = models.TextField(max_length=10)
    lge_riv = models.TextField(max_length=10)
    lk_imp_pnd = models.TextField(max_length=10)
    swp_msh_by = models.TextField(max_length=10)
    coast_ocea = models.TextField(max_length=10)
    riffles = models.TextField(max_length=10)
    run_flopool = models.TextField(max_length=10)
    pool_bckwtr = models.TextField(max_length=10)
    benthic = models.TextField(max_length=10)
    surface = models.TextField(max_length=10)
    nrshre_litt = models.TextField(max_length=10)
    opnwtr_pelag = models.TextField(max_length=10)
    mud_slt_det = models.TextField(max_length=10)
    sand = models.TextField(max_length=10)
    gravel = models.TextField(max_length=10)
    rck_rub_bol = models.TextField(max_length=10)
    vegatation = models.TextField(max_length=10)
    wdyd_brush = models.TextField(max_length=10)
    clearwater = models.TextField(max_length=10)
    turbidwater = models.TextField(max_length=10)
    warmwater = models.TextField(max_length=10)
    coolwater = models.TextField(max_length=10)
    coldwater = models.TextField(max_length=10)
    lowlands_lgr = models.TextField(max_length=10)
    uplands_hgr = models.TextField(max_length=10)
    locat_notes = models.TextField(max_length=10)
    habit_notes = models.TextField(max_length=10)

    def get_attributes(self):
        attrib = dict()
        attrib['speciesid'] = self.speciesid
        attrib['genusid'] = self.genusid
        attrib['genus'] = self.genus
        attrib['species'] = self.species
        attrib['commonname'] = self.commonname
        attrib['family'] = self.family
        attrib['group'] = self.grp
        attrib['native'] = self.native
        attrib['pfg_page'] = self.pfg_page
        attrib['sportfishing'] = self.sportfishing
        attrib['nongame'] = self.nongame
        attrib['subsis_fish'] = self.subsis_fish
        attrib['pollut_tol'] = self.pollut_tol
        attrib['max_length'] = self.max_length
        attrib['mean_length'] = self.mean_length
        attrib['mean_weight'] = self.mean_weight
        attrib['thinning'] = self.thinning
        attrib['thin_adj'] = self.thin_adj
        attrib['max_age'] = self.max_age
        attrib['w_l_a'] = self.w_l_a
        attrib['w_l_b'] = self.w_l_b
        attrib['l_w_c'] = self.l_w_c
        attrib['l_w_d'] = self.l_w_d
        attrib['regress'] = self.regress
        attrib['rarity'] = self.rarity
        attrib['caves'] = self.caves
        attrib['springs'] = self.springs
        attrib['headwaters'] = self.headwaters
        attrib['creeks'] = self.creeks
        attrib['small_riv'] = self.small_riv
        attrib['med_riv'] = self.med_riv
        attrib['lge_riv'] = self.lge_riv
        attrib['lk_imp_pnd'] = self.lk_imp_pnd
        attrib['swp_msh_by'] = self.swp_msh_by
        attrib['coast_ocea'] = self.coast_ocea
        attrib['riffles'] = self.riffles
        attrib['run_flopool'] = self.run_flopool
        attrib['pool_bckwtr'] = self.pool_bckwtr
        attrib['benthic'] = self.benthic
        attrib['surface'] = self.surface
        attrib['nrshre_litt'] = self.nrshre_litt
        attrib['opnwtr_pelag'] = self.opnwtr_pelag
        attrib['mud_slt_det'] = self.mud_slt_det
        attrib['sand'] = self.sand
        attrib['gravel'] = self.gravel
        attrib['rck_rub_bol'] = self.rck_rub_bol
        attrib['vegatation'] = self.vegatation
        attrib['wdyd_brush'] = self.wdyd_brush
        attrib['clearwater'] = self.clearwater
        attrib['turbidwater'] = self.turbidwater
        attrib['warmwater'] = self.warmwater
        attrib['coolwater'] = self.coolwater
        attrib['coldwater'] = self.coldwater
        attrib['lowlands_lgr'] = self.lowlands_lgr
        attrib['uplands_hgr'] = self.uplands_hgr
        attrib['locat_notes'] = self.locat_notes
        attrib['habit_notes'] = self.habit_notes
        return attrib

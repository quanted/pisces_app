from django.db import models

class FishSpeciesProperties(models.Model):
    """Model class for Fish Species Properties"""

    SpeciesID = models.IntegerField(primary_key=True)
    GenusID = models.IntegerField
    Genus = models.TextField(max_length=25)
    Species = models.TextField(max_length=25)
    CommonName = models.TextField(max_length=50)
    Group = models.TextField(max_length=50)
    Native = models.CharField
    PFG_Page = models.IntegerField
    Sportfishing = models.TextField(max_length=1)
    NonGame = models.TextField(max_length=1)
    Subsis_Fish = models.TextField(max_length=1)
    Pollut_Tol = models.TextField(max_length=100)
    Max_Size = models.FloatField
    Rarity = models.IntegerField
    Caves = models.TextField(max_length=10)
    Springs = models.TextField(max_length=10)
    Headwaters = models.TextField(max_length=10)
    Creeks = models.TextField(max_length=10)
    Small_Riv = models.TextField(max_length=10)
    Med_Riv = models.TextField(max_length=10)
    Lge_Riv = models.TextField(max_length=10)
    Lk_Imp_Pnd = models.TextField(max_length=10)
    Swp_Msh_By = models.TextField(max_length=10)
    Coast_Ocea = models.TextField(max_length=10)
    Riffles = models.TextField(max_length=10)
    Run_FloPool = models.TextField(max_length=10)
    Pool_Bckwtr = models.TextField(max_length=10)
    Benthic = models.TextField(max_length=10)
    Surface = models.TextField(max_length=10)
    NrShre_Litt = models.TextField(max_length=10)
    OpnWtr_Pelag = models.TextField(max_length=10)
    Mud_Slt_Det = models.TextField(max_length=10)
    Sand = models.TextField(max_length=10)
    Gravel = models.TextField(max_length=10)
    Rck_Rub_Bol = models.TextField(max_length=10)
    Vegatation = models.TextField(max_length=10)
    WdyD_Brush = models.TextField(max_length=10)
    ClearWater = models.TextField(max_length=10)
    TurbidWater = models.TextField(max_length=10)
    WarmWater = models.TextField(max_length=10)
    CoolWater = models.TextField(max_length=10)
    ColdWater = models.TextField(max_length=10)
    Lowlands_LGr = models.TextField(max_length=10)
    Uplands_HGr = models.TextField(max_length=10)
    Locat_Notes = models.TextField(max_length=10)
    Habit_Notes = models.TextField(max_length=10)
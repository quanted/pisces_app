from pisces_app.models.fish_genus_properties import FishGenusProperties
from pisces_app.models.fish_species_properties import FishSpeciesProperties
from pisces_app.models.ecoregions import EcoRegions

def get_fish_by_huc(hucIDs):
    """
    Arg1: List of NHDPlus 8 digit HUC ID.  Include leading zeros
    Returns: List of fish and associated properties from FishProperties (by species)    
    and properties by genus.
    """

    print("HUCS:" + hucIDs)
    # If there are no hucs, no reason to continue
    if not hucIDs:
        return []

    try:

        query = ("select fishproperties.CommonName, fishproperties.Genus, fishproperties.Species, "
                 "fishproperties.Max_Size, fishhucs.HUC, genera.* "
                 "from fishproperties join fishhucs on fishproperties.SpeciesID=fishhucs.SpeciesID "
                 "join genera on fishproperties.GenusID=genera.GenusID where ")

        whereClause = "fishhucs.HUC='{0}'"
        count = 0
        for huc in hucIDs:
            count = count + 1
            query = query + str.format(whereClause, huc)
            if count != len(hucIDs):
                query = query + " or "

        #conn_string = "host='172.20.100.14' dbname='pisces' user='cgifadmin' password='Ptfocns17!cgi5'"

        fish_props = list()
        for fish_prop in FishGenusProperties.objects.raw(query):
            fish_props.append(fish_prop)

        return fish_props


    except:
        pass
        # logging.error(sys.exc_info()[0])

    return None


def get_fish_range_by_species(specieIDs):
    """
    Arg1: List of fish species ids.
    Returns: List of HUCS
    """

    #   If there are no species, no reason to continue
    if not specieIDs:
        return []

    try:

        query = "select * from FishProperties where "

        whereClause = "SpeciesID ='{0}'"
        count = 0
        for specieID in specieIDs:
            count = count + 1
            query = query + str.format(whereClause, specieID)
            if count != len(specieIDs):
                query = query + " or "

        fish_props = list()
        for fish_prop in FishSpeciesProperties.objects.raw(query):
            fish_props.append(fish_prop)

        return fish_props

    except:
        pass
        # logging.error(sys.exc_info()[0])

    return None

def get_ecoregion_from_lat_lng(lat, long):
    """Return the EcoRegion containing the give coordinate"""

    try:
        print('Inside get_ecoregion_from_lat_lng - latitude: ' + lat + ', longitude: ' + long)
        point = str.format('POINT({0} {1})', long, lat)
        query = str.format("SELECT gid, aggregated from wsaecoregions where st_contains(geom, ST_GeomFromText('{0}', 4326))", point)

        print('Query: ' + query)
        eco_regions = list()
        for eco_region in EcoRegions.objects.raw(query):
            eco_regions.append(eco_region)

        return eco_regions

    except Exception as inst:
        print ("Exception: " + inst.message)
        pass


    return None
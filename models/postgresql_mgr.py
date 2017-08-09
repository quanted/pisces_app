from .fish_genus_properties import FishGenusProperties
from .fish_species_properties import FishSpeciesProperties
from .fish_names import FishNames
from .hucs import Hucs
from .ecoregions import EcoRegions

def query_species_by_huc(huc_id):
    """
        Arg1: Value of NHDPlus 8 digit HUC ID.  Include leading zeros
        Returns: List of species IDS and associated common and scientific names
        """
    # If there is no huc, no reason to continue
    if not huc_id:
        return None

    try:

        query = (
            "select fishproperties.SpeciesID, fishproperties.CommonName, fishproperties.Species, fishproperties.genus "       
            "from fishproperties join fishhucs on fishproperties.SpeciesID=fishhucs.SpeciesID where "
            "fishhucs.HUC='{0}'")

        query = query.format(huc_id)

        print('Query: ' + query)
        fish_props = list()
        for fish_prop in FishNames.objects.raw(query):
            fish_props.append(fish_prop)

        return fish_props

    except Exception as inst:
        print ("Exception: " + inst.message)

    return None


def query_genera_by_huc(huc_id):
    """
        Arg1: Value of NHDPlus 8 digit HUC ID.  Include leading zeros
        Returns: List of genus properies as well as species IDS and associated common and scientific names
        """
    # If there is no huc, no reason to continue
    if not huc_id:
        return None

    try:

        query = (
            "select fishproperties.SpeciesID, fishproperties.CommonName, fishproperties.Genus, fishproperties.Species, "
            "fishproperties.mean_weight, fishproperties.thinning, fishproperties.thin_adj, fishproperties.rarity, fishhucs.HUC, genera.* "
            "from fishproperties join fishhucs on fishproperties.SpeciesID=fishhucs.SpeciesID "
            "join genera on fishproperties.GenusID=genera.GenusID where fishhucs.HUC = '{0}'")

        #whereClause = "fishhucs.HUC='{0}'"

        query = query.format(huc_id)

        print('Query: ' + query)
        fish_props = list()
        for fish_prop in FishGenusProperties.objects.raw(query):
            fish_props.append(fish_prop)

        return fish_props

    except Exception as inst:
        print ("Exception: " + inst.message)

    return None


def query_hucs_by_species(speciesid):
    """
    Arg1: Fish species id.
    Returns: List of HUCS
    """

    #   If there are no species, no reason to continue
    if not speciesid:
        return []

    try:

        query = ("select fishproperties.SpeciesID, fishhucs.HUC from fishproperties join fishhucs on fishproperties.SpeciesID=fishhucs.SpeciesID "
                "where fishproperties.SpeciesID={0}")
        query = str.format(query, speciesid)


        hucs = list()
        for huc in Hucs.objects.raw(query):
            hucs.append(huc)

        return hucs

    except:
        pass
        # logging.error(sys.exc_info()[0])

    return None


def query_fish_properties_by_species(speciesid):
    """
        Arg1: Fish species id.
        Returns: All fish properties from FishProperties for requested species
        """

    #   If there are no species, no reason to continue
    if not speciesid:
        return []

    try:

        query = (
        "select * from fishproperties "
        "where fishproperties.SpeciesID={0}")
        query = str.format(query, speciesid)

        fish_props = list()
        for fish_prop in FishSpeciesProperties.objects.raw(query):
            fish_props.append(fish_prop)

        return fish_props

    except:
        pass
        # logging.error(sys.exc_info()[0])

    return None



def query_fish_names_by_search_string(search_string):
    """
        Arg1: Fish species id.
        Returns: common name, scientific name and genus for requested species
        """

    #   If there is no search_string, no reason to continue
    if not search_string:
        return []

    try:

        like_str = "'%%{0}%%'".format(search_string)

        query = ("select fishproperties.speciesid, fishproperties.commonname, fishproperties.species, fishproperties.genus "
                "from fishproperties where LOWER(commonname) LIKE "
                "LOWER({0}) or LOWER(species) LIKE LOWER({1}) or LOWER(genus) "
                "LIKE LOWER({2})")

        query = str.format(query, like_str, like_str, like_str)

        print(query)

        fish_props = list()
        for fish_prop in FishNames.objects.raw(query):
            fish_props.append(fish_prop)

        return fish_props

    except Exception as ex:
        print("Database error: {0}".format(ex))
        pass
        # logging.error(sys.exc_info()[0])

    return None



def query_fish_by_huc(hucIDs):
    """
    Arg1: List of NHDPlus 8 digit HUC ID.  Include leading zeros
    Returns: List of fish and associated properties from FishProperties (by species)    
    and properties by genus.
    """

    #print("HUCS:" + hucIDs)
    # If there are no hucs, no reason to continue
    if not hucIDs:
        return []

    try:

        query = ("select fishproperties.SpeciesID, fishproperties.CommonName, fishproperties.Genus, fishproperties.Species, "
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

        print('Query: ' + query)
        fish_props = list()
        for fish_prop in FishGenusProperties.objects.raw(query):
            fish_props.append(fish_prop)

        return fish_props



    except Exception as inst:
        print ("Exception: " + inst.message)

    return None


def query_fish_range_by_species(specieIDs):
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

def query_ecoregion_from_lat_lng(lat, long):
    """Return the EcoRegion containing the give coordinate"""

    try:
        #print('Inside get_ecoregion_from_lat_lng - latitude: ' + lat + ', longitude: ' + long)
        point = str.format('POINT({0} {1})', long, lat)
        query = str.format("SELECT gid, aggregated from wsaecoregions where st_contains(geom, ST_GeomFromText('{0}', 4326))", point)

        #print('Query: ' + query)
        eco_regions = list()
        for eco_region in EcoRegions.objects.raw(query):
            eco_regions.append(eco_region)

        return eco_regions

    except Exception as inst:
        print ("Exception: " + inst.message)
        pass


    return None
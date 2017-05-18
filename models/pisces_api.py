

def get_fish_by_huc(hucIDs):
    """
    Arg1: List of NHDPlus 8 digit HUC ID.  Include leading zeros
    Returns: List of fish and associated properites in the HUCs
    """

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

        #data = sqlite_mgr.execute_select_query(query, True)
        # if (data is None):
        data = ''


    except:
        pass
        # logging.error(sys.exc_info()[0])

    return data


def get_fish_range_by_species(specieIDs):
    """
    Arg1: List of fish species ids.
    Returns: List of HUCS
    """

    #   If there are no species, no reason to continue
    if not specieIDs:
        return []

    query = "select * from FishProperties where "

    whereClause = "SpeciesID ='{0}'"
    count = 0
    for specieID in specieIDs:
        count = count + 1
        query = query + str.format(whereClause, specieID)
        if count != len(specieIDs):
            query = query + " or "

    data = ''
    #data = sqlite_mgr.execute_select_query(query, True)
    return data

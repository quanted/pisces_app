from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
import json

from .models.fish_filter_query_builder import FishProperties
from .models.postgresql_mgr import query_species_by_huc
from .models.postgresql_mgr import query_genera_by_huc
from .models.postgresql_mgr import query_hucs_by_species
from .models.postgresql_mgr import query_fish_properties_by_species
from .models.postgresql_mgr import query_fish_names_by_search_string
from .models.postgresql_mgr import query_ecoregion_from_lat_lng
from .models.postgresql_mgr import query_fish_properties_by_filter
from .models.postgresql_mgr import query_stream_segment
from .models.stream_width_regression import StreamWidthRegression

#from .models.postgresql_mgr import query_fish_names_by_species
#from .models.postgresql_mgr import query_fish_properties_by_species


from .models.fish_species_properties import FishSpeciesProperties

###########################################################################################
@require_GET
def get_species_by_huc(request, huc=''):
    """
        REST API endpoint for retrieving fish species data (species id, common name, scientific name) that
        are found in the specified HUC 8
        e.g.
        https://qedinternal.epa.gov/pisces/rest/api/v1/fish/hucs/(huc8)
    """

    huc = str(huc)
    if len(huc) != 8:
        return JsonResponse({"error": "argument error: HUC value provided was not valid, please provide a valid HUC8."
                                      " Provided value = " + huc})
    # debug print
    print(huc)
    fishes = query_species_by_huc(huc)

    data = dict()
    data['huc'] = huc
    lst_fish= list()
    for fish in fishes:
        lst_fish.append(fish.get_attributes())

    data['species'] = lst_fish
    return JsonResponse(data)

###########################################################################################
@require_GET
def get_genera_by_huc(request, huc=''):
    """
        REST API endpoint for retrieving fish species data (species id, common name, scientific name) that
        are found in the specified HUC 8
        e.g.
        https://qedinternal.epa.gov/pisces/rest/api/v1/fish/hucs/(huc8)
    """

    huc = str(huc)
    if len(huc) != 8:
        return JsonResponse({"error": "argument error: HUC value provided was not valid, please provide a valid HUC8."
                                      " Provided value = " + huc})
    # debug print
    print(huc)
    fishes = query_genera_by_huc(huc)

    data = dict()
    data['huc'] = huc
    lst_fish= list()
    for fish in fishes:
        lst_fish.append(fish.get_attributes())

    data['species'] = lst_fish
    return JsonResponse(data)




###########################################################################################
@require_GET
def get_hucs_by_species(request, speciesid=''):
    """
        REST API endpoint for retrieving huc8 ids (e.g.040301010) that
        are found for specified species id.
        e.g.
        https://qedinternal.epa.gov/pisces/rest/api/v1/hucs/fish/(speciesid)
    """
    speciesid = str(speciesid)
    if len(speciesid) > 4:
        return JsonResponse({"error": "argument error: Species ID value provided was not valid, please provide a valid species ID."
                                      " Provided value = " + speciesid})
    # debug print
    print(speciesid)
    hucs = query_hucs_by_species(speciesid)

    data = dict()
    data['speciesid'] = speciesid
    lst_hucs = list()
    for huc in hucs:
        lst_hucs.append(huc.get_attributes())

    data['hucs'] = lst_hucs
    return JsonResponse(data)


###########################################################################################
@require_GET
def get_fish_names_by_search_string(request, searchstring=''):
    """
        REST API endpoint for retrieving species names (common name, scientific name, genus)
        for specified species id.
        e.g.
        https://qedinternal.epa.gov/pisces/rest/api/v1/hucs/fish/(speciesid)
    """

    #if len(speciesid) > 4:
    #   return JsonResponse({"error": "argument error: Species ID value provided was not valid, please provide a valid species ID."
    #                                  " Provided value = " + speciesid})
    # debug print
    print(searchstring)
    names = query_fish_names_by_search_string(searchstring)

    data = dict()
    data['search_string'] = searchstring
    lst_names = list()
    for name in names:
        lst_names.append(name.get_attributes())

    data['species'] = lst_names
    return JsonResponse(data)


###########################################################################################
@require_GET
def get_species_by_filter(request):
    """
        REST API endpoint for retrieving fish species data based on filtering criteria
        e.g.
        https://qedinternal.epa.gov/pisces/rest/api/v1/fish/properties/?commonname=mud_sunfish&native=Y&caves=1
    """
    #try:
    query_dict = request.GET.dict()
    fish_props = FishProperties()
    query = fish_props.build_query(query_dict)
    fish_props = query_fish_properties_by_filter(query)

    data = dict()
    lst_props = list()
    for fish_prop in fish_props:
        lst_props.append(fish_prop.get_attributes())

    data['species'] = lst_props
    return JsonResponse(data)

    #except Exception as ex:
    #    msg = ex

    #return JsonResponse("{fail}")


###########################################################################################
@require_GET
def get_stream_properties(request):
    """
        REST API endpoint for retrieving stream properties
        Get NHDplus attributes and eco region to compute streamwidth
        e.g.
        https://qedinternal.epa.gov/pisces/rest/api/v1/stream/properties?latitude=X&longitude=Y&comid=NUM
    """
    query_dict = request.GET.dict()
    latitude = query_dict['latitude']
    longitude = query_dict['longitude']
    comid = query_dict['comid']

    return_data = dict()

    #Get the ecoregion from a lat/long
    lst_eco_region_models = query_ecoregion_from_lat_lng(latitude, longitude)

    lst_eco_regions = []
    for region in lst_eco_region_models:
        lst_eco_regions.append(region.get_attributes())

    if len(lst_eco_region_models) < 1:
        return JsonResponse({"error: no valid ecoregion"})

    eco_region_gid = None
    eco_region_gid = lst_eco_region_models[0].gid

    lst_stream_seg = []
    lst_stream_seg_models = query_stream_segment(comid)
    for seg in lst_stream_seg_models:
        lst_stream_seg.append(seg.get_attributes())

    slope = None
    drainage_area = None
    precip = None
    elev = None
    slope = lst_stream_seg[0]['slope']
    if (slope < 1.001e-5) and (slope > 0):
        slope = 1.001e-5

    if len(lst_stream_seg) > 0:
        #Multiply by 100 to go from percent - round to 2 digits
        #slope = round((lst_stream_seg[0]['slope'] * 100),2)
        slope = slope * 100
        # round to nearest int
        drainage_area = round(lst_stream_seg[0]['totdasqkm'])
        drainage_area = drainage_area / 100.0
        precip = lst_stream_seg[0]['precipvc']
        precip = precip / 100000.0
        #elev = lst_stream_seg[0]['mavelv']
        elev =  (lst_stream_seg[0]['maxelevsmo'] + lst_stream_seg[0]['minelevsmo']) / 2.0
        elev = elev / 100.0

    stream_width_reg = StreamWidthRegression()
    stream_width = stream_width_reg.calculate_stream_width(eco_region_gid, drainage_area, precip, slope, elev)
    fine_width = stream_width['fine']
    course_width = stream_width['course']
    avg_width = (fine_width + course_width) / 2.0

    attributes = {'width':avg_width,
                  'fine_width' : fine_width,
                  'course_width' : course_width,
                  'area':drainage_area, 
                  'slope':slope, 
                  'precipitation':precip, 
                  'elevation': elev,
                  'eco_region':eco_region_gid}

    data = {}
    data['comid'] = comid
    data['attributes']= attributes
    return JsonResponse(data)


###########################################################################################
@require_POST
def post_fish_names_by_species(request):
    """
        REST API endpoint for retrieving species names (common name, scientific name, genus)
        for specified species id.
        e.g.
        https://qedinternal.epa.gov/pisces/rest/api/v1/fish/properties/names
    """
    search = json.loads(request.body, encoding='utf-8')
    searchstring = search['search_string']

    names = query_fish_names_by_search_string(searchstring)

    data = dict()
    data['search_string'] = searchstring
    lst_names = list()
    for name in names:
        lst_names.append(name.get_attributes())

    data['species'] = lst_names
    return JsonResponse(data)


###########################################################################################
@require_GET
def get_fish_properties_by_species(request, speciesid=''):
    """
        REST API endpoint for retrieving species names (common name, scientific name, genus)
        for specified species id.
        e.g.
        https://qedinternal.epa.gov/pisces/rest/api/v1/fish/properties/names/search_string
    """

    speciesid = str(speciesid).strip()
    if len(speciesid) > 4:
        return JsonResponse({"error": "argument error: Species ID value provided was not valid, please provide a valid species ID."
                                      " Provided value = " + speciesid})
    # debug print
    print(speciesid)
    fish_props = query_fish_properties_by_species(speciesid)

    data = dict()
    data['speciesid'] = speciesid
    lst_props = list()
    for fish_prop in fish_props:
        lst_props.append(fish_prop.get_attributes())

    data['species'] = lst_props
    return JsonResponse(data)



# @require_POST
# def post_species_by_huc(request):
#     """
#         REST API endpoint for retrieving fish species data (species id, common name, scientific name) that
#         are found in the specified HUC 8
#         e.g.
#         {"huc8":"04030101"}
#     """
#     huc = json.loads(request.body, encoding='utf-8')
#
#     # debug print
#     print(huc)
#     huc8 = huc['huc8']
#     fishes = query_get_species_by_huc(huc8)
#
#     data = dict()
#     data['huc'] = huc8
#     lst_fish= list()
#     for fish in fishes:
#         lst_fish.append(fish.get_attributes())
#
#     data['species'] = lst_fish
#     return JsonResponse(data)

# @require_POST
# def post_species_by_huc(request):
#     """
#         REST API endpoint for retrieving fish species data (species id, common name, scientific name) that
#         are found in the specified HUC 8
#         e.g.
#         {
#             "huc":"04030101"
#         }
#     """
#     huc = json.loads(request.body, encoding='utf-8')
#
#     # debug print
#     print(huc)
#     huc8 = huc['huc']
#     fishes = query_get_species_by_huc(huc8)
#
#     data = dict()
#     data['huc'] = huc8
#     lst_fish= list()
#     for fish in fishes:
#         lst_fish.append(fish.get_attributes())
#
#     data['species'] = lst_fish
#     return JsonResponse(data)

# @require_POST
# def get_fish_properties_by_huc(request):
#     """   """
#     if request.method == 'GET':
#         return HttpResponse(status=404)
#
#     #debug print
#     print(request.body)
#     hucs = json.loads(request.body, encoding='utf-8')
#
#     # debug print
#     print(hucs)
#     huc_list = []
#     for huc in hucs:
#         huc_list.append(hucs[huc])
#
#     results = dict()
#     fish_props = query_fish_by_huc(hucs)
#     for fish_prop in fish_props:
#         results[fish_prop.species] = fish_prop.get_attributes()
#
#     return HttpResponse(json.dumps(results))
#
#
# def get_fish_range_by_species(request):
#     """   """
#     if request.method == 'GET':
#         return HttpResponse(status=404)
#
#     species = json.loads(request.body, encoding='utf-8')
#     for sp in species:
#         s = sp
#
#     ranges = query_fish_range_by_species(species)
#
#     return HttpResponse(ranges)


def get_ecoregion_from_pt(request):
    """   """
    if request.method == 'GET':
        return HttpResponse(status=404)

    # debug print
    print(request.body)
    body_unicode = request.body.decode('utf-8')
    # debug print
    print(body_unicode)

    pt = json.loads(body_unicode)

    latitude = pt['latitude']
    longitude = pt['longitude']

    print('latitude: ' + latitude + ', longitude: ' + longitude)
    eco_range = query_ecoregion_from_lat_lng(latitude, longitude)

    print('Length of eco_range list: {}'.format(len(eco_range)))
    dct_range = dict()
    for range in eco_range:
        print(dir(range))
        dct_range['gid'] = range.gid
        dct_range['region'] = range.aggregated
        break

    return HttpResponse(json.dumps(dct_range))

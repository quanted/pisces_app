from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
import json

from .models.postgresql_mgr import query_fish_by_huc
from .models.postgresql_mgr import query_fish_range_by_species
from .models.postgresql_mgr import query_ecoregion_from_lat_lng
from .models.postgresql_mgr import query_get_species_by_huc

from .models.fish_species_properties import FishSpeciesProperties

@require_GET
def get_species_by_huc(request, huc8=''):
    """
        REST API endpoint for retrieving fish species data (species id, common name, scientific name) that
        are found in the specified HUC 8
        e.g.
        https://qedinternal.epa.gov/pisces/rest/api/v1/(huc8)
    """

    if len(huc8) != 4:
        return JsonResponse({"error": "argument error: HUC* value provided was not valid, please provide a valid HUC8."
                                      " Provided value = " + huc8})
    # debug print
    print(huc8)
    fishes = query_get_species_by_huc(huc8)

    data = dict()
    data['huc'] = huc8
    lst_fish= list()
    for fish in fishes:
        lst_fish.append(fish.get_attributes())

    data['species'] = lst_fish
    return JsonResponse(data)


@require_POST
def post_species_by_huc(request):
    """
        REST API endpoint for retrieving fish species data (species id, common name, scientific name) that
        are found in the specified HUC 8
        e.g.
        {"huc8":"04030101"}
    """
    huc = json.loads(request.body, encoding='utf-8')

    # debug print
    print(huc)
    huc8 = huc['huc8']
    fishes = query_get_species_by_huc(huc8)

    data = dict()
    data['huc'] = huc8
    lst_fish= list()
    for fish in fishes:
        lst_fish.append(fish.get_attributes())

    data['species'] = lst_fish
    return JsonResponse(data)

@require_POST
def post_species_by_huc(request):
    """
        REST API endpoint for retrieving fish species data (species id, common name, scientific name) that
        are found in the specified HUC 8
        e.g.
        {
            "huc":"04030101"
        }
    """
    huc = json.loads(request.body, encoding='utf-8')

    # debug print
    print(huc)
    huc8 = huc['huc']
    fishes = query_get_species_by_huc(huc8)

    data = dict()
    data['huc'] = huc8
    lst_fish= list()
    for fish in fishes:
        lst_fish.append(fish.get_attributes())

    data['species'] = lst_fish
    return JsonResponse(data)

@require_POST
def get_fish_properties_by_huc(request):
    """   """
    if request.method == 'GET':
        return HttpResponse(status=404)

    #debug print
    print(request.body)
    hucs = json.loads(request.body, encoding='utf-8')

    # debug print
    print(hucs)
    for huc in hucs:
        h = huc

    results = dict()
    fish_props = query_fish_by_huc(hucs)
    for fish_prop in fish_props:
        results[fish_prop.species] = fish_prop.get_attributes()

    return HttpResponse(json.dumps(results))


def get_fish_range_by_species(request):
    """   """
    if request.method == 'GET':
        return HttpResponse(status=404)

    species = json.loads(request.body, encoding='utf-8')
    for sp in species:
        s = sp

    ranges = query_fish_range_by_species(species)

    return HttpResponse(ranges)


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
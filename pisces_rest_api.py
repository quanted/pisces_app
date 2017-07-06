from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

#from models.sqlite_mgr import get_fish_by_huc
from .models.postgresql_mgr import get_fish_by_huc
#from .models.sqlite_mgr import get_fish_range_by_species
from .models.postgresql_mgr import get_fish_range_by_species
#from .models.sqlite_mgr import get_ecoregion_from_lat_lng
from .models.postgresql_mgr import get_ecoregion_from_lat_lng
from .models.fish_species_properties import FishSpeciesProperties

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
    fish_props = get_fish_by_huc(hucs)
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

    ranges = get_fish_range_by_species(species)

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
    eco_range = get_ecoregion_from_lat_lng(latitude, longitude)

    print('Length of eco_range list: {}'.format(len(eco_range)))
    dct_range = dict()
    for range in eco_range:
        print(dir(range))
        dct_range['gid'] = range.gid
        dct_range['region'] = range.aggregated
        break

    return HttpResponse(json.dumps(dct_range))
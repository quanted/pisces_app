from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from models.sqlite_mgr import get_fish_by_huc
from models.sqlite_mgr import get_fish_range_by_species
from models.sqlite_mgr import get_ecoregion_from_lat_lng
from models.fish_species_properties import FishSpeciesProperties

def get_fish_properties_by_huc(request):
    """   """
    if request.method == 'GET':
        return HttpResponse(status=404)

    hucs = json.loads(request.body, encoding='utf-8')
    for huc in hucs:
        h = huc

    fish_props = get_fish_by_huc(hucs)

    return HttpResponse(fish_props)


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

    #pt = json.loads(request.body, encoding='utf-8')
    body_unicode = request.body.decode('utf-8')
    pt = json.loads(body_unicode)
    #pt = request.body
    latitude = pt['latitude']
    longitude = pt['longitude']

    eco_range = get_ecoregion_from_lat_lng(latitude, longitude)

    return HttpResponse(eco_range)
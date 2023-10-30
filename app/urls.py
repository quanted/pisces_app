"""
Definition of urls for qed_pisces.
"""

from datetime import datetime
# from django.conf.urls import url
from django.urls import path, include
import django.contrib.auth.views

from . import pisces_rest_api, views, description, watershed
from . import stream, species_explorer, algorithms, references, contact


urlpatterns = [
    # ----- Django 1.11 urls ----- #
    # front end urls
    # url(r'^$', description.description_page, {'model': 'pisces'}),
    # url(r'^watershed/$', watershed.watershed_page, {'model': 'pisces'}),
    # # url(r'^stream/$', stream.stream_page, {'model': 'pisces'}),
    # url(r'^stream/$', stream.stream_page_v2, {'model': 'pisces'}),
    # url(r'^species/$', species_explorer.query_page, {'model': 'pisces'}),
    # url(r'^algorithms/$', algorithms.algorithm_page, {'model': 'pisces'}),
    # url(r'^references/$', references.references_page, {'model': 'pisces'}),

    path('contact/', contact.contact_page),
    path('contact/comment/', contact.handle_contact_post),
    # # url(r'^api$', rest.rest_page, {'model': 'pisces'}),
    # # url(r'^swag$', views.getSwaggerJsonContent)
    #
    # rest urls
    # url(r'^rest/api/v1/fish/hucs/(?P<huc>\w+)/$', pisces_rest_api.get_species_by_huc),
    # url(r'^rest/api/v1/fish/genera/hucs/(?P<huc>\w+)/$', pisces_rest_api.get_genera_by_huc),
    # url(r'^rest/api/v2/fish/genera/hucs/(?P<huc>\w+)/$', pisces_rest_api.get_genera_by_huc_v2),
    # url(r'^rest/api/v1/hucs/fish/(?P<speciesid>\w+)/$', pisces_rest_api.get_hucs_by_species),
    # url(r'^rest/api/v1/fish/properties/names/$', pisces_rest_api.post_fish_names_by_species),
    # url(r'^rest/api/v1/fish/properties/names/(?P<searchstring>\w+)/$', pisces_rest_api.get_fish_names_by_search_string),
    # url(r'^rest/api/v1/fish/properties/(?P<speciesid>\w+)/$', pisces_rest_api.get_fish_properties_by_species),
    #
    # # Example querystring
    # # rest/api/v1/fish/properties/?commonname=mud_sunfish&native=Y&caves=1
    # url(r'^rest/api/v1/fish/properties/$', pisces_rest_api.get_species_by_filter),
    # url(r'^rest/api/v1/stream/properties/$', pisces_rest_api.get_stream_properties),
    # url(r'^rest/api/v1/ecoregions/$', pisces_rest_api.get_ecoregion_from_pt),

    # ----- Django 2.0 urls ----- #
    # front end urls
    path('', description.description_page, {'model': 'pisces'}),
    path('watershed/', watershed.watershed_page, {'model': 'pisces'}),
    path('stream/', stream.stream_page_v2, {'model': 'pisces'}),
    path('species/', species_explorer.query_page, {'model': 'pisces'}),
    path('algorithms/', algorithms.algorithm_page, {'model': 'pisces'}),
    path('references/', references.references_page, {'model': 'pisces'}),

    # rest urls
    path('rest/api/v1/fish/hucs/<str:huc>/', pisces_rest_api.get_species_by_huc),
    path('rest/api/v1/fish/genera/hucs/<str:huc>/', pisces_rest_api.get_genera_by_huc),
    path('rest/api/v2/fish/genera/hucs/<str:huc>/', pisces_rest_api.get_genera_by_huc_v2),
    path('rest/api/v1/hucs/fish/<int:speciesid>/', pisces_rest_api.get_hucs_by_species),
    path('rest/api/v1/fish/properties/names/', pisces_rest_api.post_fish_names_by_species),
    path('rest/api/v1/fish/properties/names/<str:searchstring>/', pisces_rest_api.get_fish_names_by_search_string),
    path('rest/api/v1/fish/properties/<int:speciesid>/', pisces_rest_api.get_fish_properties_by_species),

    # Example querystring
    # rest/api/v1/fish/properties/?commonname=mud_sunfish&native=Y&caves=1
    path('rest/api/v1/fish/properties/', pisces_rest_api.get_species_by_filter),
    path('rest/api/v1/stream/properties/', pisces_rest_api.get_stream_properties),
    path('rest/api/v1/ecoregions/', pisces_rest_api.get_ecoregion_from_pt),

    path('rest/api/v2/fish/models/', pisces_rest_api.run_species_models)

]

urlpatterns = [path('pisces/', include(urlpatterns))]


# 404 Error view (file not found)
handler404 = views.file_not_found
# 500 Error view (server error)
handler500 = views.file_not_found
# 403 Error view (forbidden)
handler403 = views.file_not_found

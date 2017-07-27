"""
Definition of urls for qed_pisces.
"""

from datetime import datetime
from django.conf.urls import url

import django.contrib.auth.views

from . import pisces_rest_api, views, description, watershed
from . import stream, species_explorer, algorithms, references, links_left


# if settings.IS_PUBLIC:
urlpatterns = [
    # url(r'^$', views.pisces_landing_page),
    #front end urls
    url(r'^$', description.description_page, {'model': 'pisces'}),
    url(r'^watershed$', watershed.watershed_page, {'model': 'pisces'}),
    url(r'^stream$', stream.stream_page, {'model': 'pisces'}),
    url(r'^species$', species_explorer.query_page, {'model': 'pisces'}),
    url(r'^algorithms/$', algorithms.algorithm_page, {'model': 'pisces'}),
    url(r'^references/$', references.references_page, {'model': 'pisces'}),
    # url(r'^api$', rest.rest_page, {'model': 'pisces'}),
    # url(r'^swag$', views.getSwaggerJsonContent)

    # rest urls
    url(r'^rest/api/v1/fish/hucs/(?P<huc>\w+)$', pisces_rest_api.get_species_by_huc),
    url(r'^rest/api/v1/hucs/fish/(?P<speciesid>\w+)$', pisces_rest_api.get_hucs_by_species),
    url(r'^rest/api/v1/fish/properties/names/(?P<searchstring>\w+)$', pisces_rest_api.get_fish_names_by_search_string),
    url(r'^rest/api/v1/fish/properties/(?P<speciesid>\w+)$', pisces_rest_api.query_fish_properties_by_species),


    #url(r'^rest/api/v1/fishproperties$', pisces_rest_api.get_fish_properties_by_huc),
    #url(r'^rest/api/v1/fishranges$', pisces_rest_api.get_fish_range_by_species),
    url(r'^rest/api/v1/ecoregions$', pisces_rest_api.get_ecoregion_from_pt)
]
# else:
#     urlpatterns = [
#         #url(r'^api/', include('api.urls')),
#         #url(r'^rest/', include('REST.urls')),
#         url(r'^$', views.cyan_landing_page),
#         #url(r'^$', views.qed_splash_page_intranet),
#         # url(r'^admin/', include(admin.site.urls)),
#     ]

# 404 Error view (file not found)
handler404 = views.file_not_found
# 500 Error view (server error)
handler500 = views.file_not_found
# 403 Error view (forbidden)
handler403 = views.file_not_found

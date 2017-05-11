"""
Definition of urls for qed_pisces.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import views
import description
import watershed
import stream
import algorithms
import references
import links_left

# if settings.IS_PUBLIC:
urlpatterns = [
    # url(r'^$', views.pisces_landing_page),
    #front end urls
    url(r'^$', description.description_page, {'model': 'pisces'}),
    url(r'^watershed$', watershed.watershed_page, {'model': 'pisces'}),
    url(r'^stream$', stream.stream_page, {'model': 'pisces'}),
    url(r'^algorithms$', algorithms.algorithm_page, {'model': 'pisces'}),
    url(r'^references$', references.references_page, {'model': 'pisces'}),
    # url(r'^api$', rest.rest_page, {'model': 'pisces'}),
    # url(r'^swag$', views.getSwaggerJsonContent)
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
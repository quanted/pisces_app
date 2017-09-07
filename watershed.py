from django.template.loader import render_to_string
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from django.conf import settings
from . import links_left
from pisces_app import views
from pisces_app import stream


@ensure_csrf_cookie
def watershed_page(request, model='pisces', header='none'):
    header = views.header
    x = render_to_string('pisces_watershed_map.html', request=request)

    """ Returns the html of the references page for pisces. """
    html = render_to_string('01pisces_epa_drupal_header.html', {})
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})
    html += stream.stream_ordered_list(model, 'streammap')
    html += render_to_string('04pisces_watershed_text_start_index_drupal.html', {
        'TITLE': header + ' Distribution Explorer',
        'TEXT_PARAGRAPH': x})

    html += render_to_string('04ubertext_end_drupal.html', {})

    # html += links_left.ordered_list(model, 'watershedmap')
    html += render_to_string('10epa_drupal_footer.html', {})

    response = HttpResponse()
    response.write(html)
    return response

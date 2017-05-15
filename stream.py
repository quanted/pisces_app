from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from django.conf import settings
import links_left
from pisces_app import views



def stream_page(request, model='pisces', header='none'):
    header = views.header
    x = render_to_string('pisces_stream_map.html')

    """ Returns the html of the references page for pisces. """
    html = render_to_string('01epa_drupal_header.html', {})
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03epa_drupal_section_title.html', {})

    html += render_to_string('04ubertext_start_index_drupal.html', {
        'TITLE': header + ' Assemblage Predictor',
        'TEXT_PARAGRAPH': x})

    html += render_to_string('04ubertext_end_drupal.html', {})

    html += links_left.ordered_list(model, 'streammap')
    html += render_to_string('10epa_drupal_footer.html', {})
    # html = x

    response = HttpResponse()
    response.write(html)
    return response
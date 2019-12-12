from django.template.loader import render_to_string
from django.http import HttpResponse
from collections import OrderedDict
from django.shortcuts import redirect
import os
from django.conf import settings
from . import links_left
from . import views



def stream_page(request, model='pisces', header='none'):
    header = views.header
    eco_url = "https://qedinternal.epa.gov/pisces/rest/ecoregion"
    x = render_to_string('pisces_stream_map.html', {
        'ECO_URL': eco_url
    })

    """ Returns the html of the references page for pisces. """
    html = render_to_string('01pisces_epa_drupal_header.html', {})
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03pisces_drupal_section_title.html', {})
    html += stream_ordered_list(model, 'streammap')

    html += render_to_string('04pisces_stream_text_start_index_drupal.html', {
        'TITLE': 'Stream Fish Assemblage Predictor',
        'TEXT_PARAGRAPH': x})

    html += render_to_string('04ubertext_end_drupal.html', {})

    # html += stream_ordered_list(model, 'streammap')
    html += render_to_string('10epa_drupal_footer.html', {})
    # html = x

    response = HttpResponse()
    response.write(html)
    return response


def stream_page_v2(request, model='pisces', header='none'):
    header = views.header
    eco_url = "https://qedinternal.epa.gov/pisces/rest/ecoregion"
    imports = render_to_string('pisces_stream_map_v2_imports.html')
    x = render_to_string('pisces_stream_map_v2.html', {
        'ECO_URL': eco_url,
        'IMPORTS': imports
    })

    """ Returns the html of the references page for pisces. """
    html = render_to_string('01pisces_epa_drupal_header.html', {})
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03pisces_drupal_section_title.html', {})
    html += stream_ordered_list(model, 'streammap')

    html += render_to_string('04pisces_stream_text_start_index_drupal.html', {
        'TITLE': 'Stream Fish Assemblage Predictor',
        'TEXT_PARAGRAPH': x})

    html += render_to_string('04ubertext_end_drupal.html', {})

    # html += stream_ordered_list(model, 'streammap')
    html += render_to_string('10epa_drupal_footer.html', {})
    # html = x

    response = HttpResponse()
    response.write(html)
    return response


def stream_ordered_list(model=None, page=None):
    link_dict = OrderedDict([
        ('Model', OrderedDict([
                ('PiSCES', 'pisces'),
            ])
         ),
        ('Documentation', OrderedDict([
                ('API Documentation', '/qedinternal.epa.gov/pisces/rest'),
                ('Source Code', '/github.com/quanted/qed_pisces'),
                ('Algorithms', 'pisces/algorithms'),
                ('References', 'pisces/references')
            ])
         )
    ])

    return render_to_string('03pisces_stream_links_left_drupal.html', {
        'LINK_DICT': link_dict,
        'MODEL': model,
        'PAGE': page
    })
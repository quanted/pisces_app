from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from django.conf import settings
from . import links_left

from . import views


def description_page(request, model='pisces', header='none'):

    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(current_dir)

    header = views.header

    xx = render_to_string('pisces_text.txt')

    """ Returns the html of the references page for pisces. """
    html = render_to_string('01epa_drupal_header.html', {})
    html += render_to_string('02epa_drupal_header_bluestripe_onesidebar.html', {})
    html += render_to_string('03pisces_drupal_main_title.html', {"TITLE": "Piscine Stream Community Estimation System"})

    html += render_to_string('04ubertext_start_index_drupal.html', {
        'TITLE': header + ' Overview',
        'TEXT_PARAGRAPH': xx})

    html += render_to_string('04ubertext_end_drupal.html', {})

    html += links_left.ordered_list(model)
    html += render_to_string('10epa_drupal_footer.html', {})


    response = HttpResponse()
    response.write(html)
    return response
from django.template.loader import render_to_string
from collections import OrderedDict
from django.shortcuts import redirect


# 03ubertext_links_left:
def ordered_list(model=None, page=None):
    link_dict = OrderedDict([
        ('Model', OrderedDict([
                ('Pisces', 'pisces'),
            ])
         ),
        ('Documentation', OrderedDict([
                ('API Documentation', '/qedinternal.epa.gov/pisces/rest'),
                ('Source Code', '/github.com/quanted/qed_pisces')
            ])
         )
    ])

    return render_to_string('03pisces_links_left_drupal.html', {
        'LINK_DICT': link_dict,
        'MODEL': model,
        'PAGE': page
    })
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
import pisces_app.links_left as links_left
import sqlite3
import os
import logging
import datetime

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
db_name = "pisces_comments.sqlite3"


def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


def create_tables(conn, create_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_sql)
    except sqlite3.Error as e:
        print(e)


def add_comment(name, email, comment):
    """
    :param name:
    :param email:
    :param comment:
    :return:
    """
    conn = create_connection()
    sql_create_table = 'CREATE TABLE IF NOT EXISTS comments (name text NOT NULL, email text NOT NULL, comment text, timestamp text)'
    create_tables(conn, sql_create_table)

    new_comment = 'INSERT INTO comments VALUES (?,?,?,?)'
    try:
        parameters = (name, email, comment, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        cur = conn.cursor()
        cur.execute(new_comment, parameters)
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error:
        return False


def handle_contact_post(request):
    """
    :param request:
    :return:
    """
    post_data = request.POST
    name = request.POST.get('name', "none") or "none"  # additional or accounts for blank string
    from_email = request.POST.get('email', "none") or "none"
    comment = request.POST.get('comment')

    try:
        add_comment(name, from_email, comment)
    except Exception as e:
        logging.warning("Exception occurred handling contact submission: {}".format(e))
        return

    return contacts_submission_view(request)


def contacts_submission_view(request):
    """
    Page that displays after an email has been sent by
    the user on the contacts page.
    :param request:
    :request:
    """
    page_title = "Piscine Stream Community Estimation System"
    keywords = "PiSCES, Piscine Stream Community Estimation System, EPA"
    imports = render_to_string('hms_default_imports.html')

    disclaimer_file = open(os.path.join(os.environ['PROJECT_PATH'], 'hms_app/views/disclaimer.txt'), 'r')
    disclaimer_text = disclaimer_file.read()
    notpublic = True

    html = render_to_string('01epa18_default_header.html', {
        'TITLE': page_title,
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': imports,
        'NOTPUBLIC': False,
        'DISCLAIMER': None
    })                                                                     # Default EPA header
    html += links_left.ordered_list(model='pisces')

    html += render_to_string('05hms_body_start.html', {
        'TITLE': "Thank you for your comments!",
        'DESCRIPTION': """An email has been sent to the PiSCES team.<br>
            If a return email address was provided, we'll get back to you as soon as possible.<br><br>
            <!--Return to <a href="/pisces">homepage</a>.-->
            <form action="/pisces" method="get">
                <input type="submit" value="Go back PiSCES homepage" />
            </form>
            """
    })                                                                      # HMS Workflow main body start
    html += render_to_string('06hms_body_end.html')                         # HMS Workflow main body end
    html += render_to_string('07hms_splashscripts.html')                    # EPA splashscripts import
    html += render_to_string('10epa_drupal_footer.html')                    # Default EPA footer
    response = HttpResponse()
    response.write(html)
    return response


def contact_page(request):
    """
    :param request:
    :return:
    """
    page_title = "Piscine Stream Community Estimation System"
    keywords = "PiSCES, Piscine Stream Community Estimation System, EPA"
    imports = render_to_string('hms_default_imports.html')

    html = render_to_string('01epa18_default_header.html', {
        'TITLE': page_title,
        'URL': str(request.get_host) + request.path,
        'KEYWORDS': keywords,
        'IMPORTS': imports,
        'NOTPUBLIC': False,
        'DISCLAIMER': None
    })                                                                     # Default EPA header
    html += links_left.ordered_list(model='pisces')
    page_text = render_to_string("04pisces_contact_body.html", {}, request=request)

    html += render_to_string('05pisces_body_start.html', {
        'TITLE': "PiSCES Contact Us",
        'DESCRIPTION': page_text
    })                                                                      # HMS Workflow main body start
    html += render_to_string('06hms_body_end.html')                         # HMS Workflow main body end
    html += render_to_string('07hms_splashscripts.html')                    # EPA splashscripts import
    html += render_to_string('10epa_drupal_footer.html')                    # Default EPA footer
    response = HttpResponse()
    response.write(html)
    return response

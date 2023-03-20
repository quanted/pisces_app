
EDIT_STATEMENTS = ['insert', 'update', 'delete', 'create', 'drop', 'backup', 'alter', ]


def clean_query(query_string):
    query_string = query_string.lower()
    for statement in EDIT_STATEMENTS:
        if statement in query_string:
            return False
    return True

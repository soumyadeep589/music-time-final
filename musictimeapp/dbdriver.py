from django.db import connection


def my_custom_sql():
    with connection.cursor() as cursor:

        cursor.execute("SELECT username FROM User WHERE  = )
        row = cursor.fetchone()

    return row
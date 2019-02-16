import os
import jinja2

MYSQL_HOST = 'sql9.freesqldatabase.com'
MYSQL_NAME = 'sql9279343'
MYSQL_USER = 'sql9279343'
MYSQL_PASSWORD = 'e1WICYN2Kc'
MYSQL_TABLE_NAME = 'CLOCK_EVENT'


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/app/views/templates")
)

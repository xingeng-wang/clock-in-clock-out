import os
import webapp2
import jinja2

from app.domain.clock_event import creat_clock_event

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates")
)


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('home.html')
        self.response.out.write(template.render())

    def post(self):
        clock_type = self.request.get('clockType')
        last_name = self.request.get('lastName')
        first_name = self.request.get('firstName')
        creat_clock_event(first_name, last_name, clock_type)
        self.response.out.write('event created!')


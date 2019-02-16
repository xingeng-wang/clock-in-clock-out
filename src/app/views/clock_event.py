import webapp2

from app.domain.clock_event import creat_clock_event, list_clock_event
from settings import JINJA_ENVIRONMENT


class CreateClockEventHandler(webapp2.RequestHandler):
    def post(self):
        clock_type = self.request.get('clockType')
        last_name = self.request.get('lastName')
        first_name = self.request.get('firstName')
        creat_clock_event(first_name, last_name, clock_type)
        template = JINJA_ENVIRONMENT.get_template('home.html')
        self.response.out.write(template.render())


class ListClockEventHandler(webapp2.RequestHandler):
    def get(self):
        result = list_clock_event()
        template = JINJA_ENVIRONMENT.get_template('event_table.html')
        self.response.out.write(template.render({'clockEvents': result}))

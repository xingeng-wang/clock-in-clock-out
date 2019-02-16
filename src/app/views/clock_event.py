import webapp2

from app.domain.clock_event import creat_clock_event, list_clock_event
from settings import JINJA_ENVIRONMENT


class CreateClockEventHandler(webapp2.RequestHandler):
    def post(self):
        clock_type = self.request.get('clockType')
        last_name = self.request.get('lastName')
        first_name = self.request.get('firstName')
        print "I am getting hit with :", first_name, last_name, clock_type
        creat_clock_event(first_name, last_name, clock_type)
        self.response.status_int = 200


class ListClockEventHandler(webapp2.RequestHandler):
    def get(self):
        print "I am getting hit the ListClockEventHandler "
        result = list_clock_event()
        # self.response.headers['Content-Type'] = 'application/json'
        # self.response.out.write(json.dumps(result))
        template = JINJA_ENVIRONMENT.get_template('home.html')
        self.response.out.write(template.render({'clockEvents': result}))

import webapp2

from ..domain.clock_event import creat_clock_event, list_clock_event
from settings import JINJA_ENVIRONMENT


class CreateClockEventHandler(webapp2.RequestHandler):
    """
    API handler for create  the clock event entity
    """
    def post(self):
        clock_type = self.request.get('clockType')
        last_name = self.request.get('lastName')
        first_name = self.request.get('firstName')
        try:
            creat_clock_event(first_name, last_name, clock_type)
            template = JINJA_ENVIRONMENT.get_template('create_event.html')
            message = '%s %s %s succeed' % (first_name, last_name, clock_type)
            self.response.out.write(template.render({'message': message}))
        except:
            template = JINJA_ENVIRONMENT.get_template('create_event.html')
            message = '%s %s Failed to %s ' % (first_name, last_name, clock_type)
            self.response.out.write(template.render({'message': message}))


class ListClockEventHandler(webapp2.RequestHandler):
    """
    API handler for retrieve the clock event entity
    """
    def get(self):
        result = list_clock_event()
        template = JINJA_ENVIRONMENT.get_template('event_table.html')
        self.response.out.write(template.render({'clockEvents': result}))

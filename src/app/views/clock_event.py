import webapp2


class CreateClockEventHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, webapp2!')

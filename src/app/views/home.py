import webapp2

from settings import JINJA_ENVIRONMENT


class HomeHandler(webapp2.RequestHandler):
    """
    API handler to render the home page template for the app
    """
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('home.html')
        self.response.out.write(template.render())


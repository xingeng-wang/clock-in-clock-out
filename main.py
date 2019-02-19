import webapp2
from routes import routes


APP = webapp2.WSGIApplication(routes=routes, debug=True)

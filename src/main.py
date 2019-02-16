import webapp2
from routes import routes
import os


APP = webapp2.WSGIApplication(routes=routes, debug=True)


def main():
    from paste import httpserver
    httpserver.serve(APP, host='127.0.0.1', port='8080')


if __name__ == '__main__':
    main()

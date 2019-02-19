This app is using webapp2 framework, which is compatible with Google App Engine.
It also use the template framework from Jinja2 library, and mysql for data storage.

The `Time` variable we store in Mysql is actually the clock event time in UTC time,
but we convert that to local time when we display that in the user side.

In order to save time on local development, I use an only sql database https://www.freesqldatabase.com
Which is good for this use case.

# How to run this in local
- this project is written in python 2.7 so make sure you have python 2.7 installed,
 here is the download link for python 2.7 https://www.python.org/downloads/release/python-2715/
- run the `virtualenv env` to create a virtual environment
- run the `. env/bin/activate` to activate the virtual environment
- run `pip install -r requirements.txt` to install the required python library
- run `gunicorn main:APP` to start the server on your local machine
- Navigate to the http://127.0.0.1:8000 on your web browser

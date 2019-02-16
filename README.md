this app is using webapp2 framework, which is compatible with Google App Engine.
It also use the template framework from Jinja2 library, and mysql for data storage.

The time we store in Mysql is actually the clock in or clock out time in UTC time,
but we convert that to local time whe we display that in the user side.

# How to run this in local
- run the `virtualenv env` to create a virtual environment
- run the `. env/bin/activate` to activate the virtual environment
- run `pip install -r requirements.txt` to install the required python library
- run `python src/main.py` to start the server on your local machine
- Navigate to the http://127.0.0.1:8080 on your web browser

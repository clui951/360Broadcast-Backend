### Main App ###
import os
from flask import Flask
import contact_book


app = Flask(__name__)

cb = contact_book.ContactBook()


################### Routes #####################

@app.route("/")
def root_page():
	return '360 Broadcast Backend Landing Page\n' + 'If you are a user, you should not be seeing this!'


@app.route("api/v1/text911")
def text911():
	return 'Texted 911; forwarding content to all contacts'


@app.route("api/v1/call911")
def call911():
	return 'Called 911; texting info to all contacts'


@app.route("api/v1/update")
def updateCB():
	return "Endpoint for updating cb"



################### Start Server #####################

if __name__ == '__main__':
    app.debug = True
    app.run()
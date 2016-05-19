### Main App ###
import os
from flask import Flask, render_template, request
import contact_book
import sanitize


app = Flask(__name__)

cb = contact_book.ContactBook()


################### Routes #####################

@app.route("/")
def root_page():
	return render_template('root_view.html'), 403


@app.route("api/v1/text911")
def text911():
	return 'Texted 911; forwarding content to all contacts'


@app.route("api/v1/call911")
def call911():
	return 'Called 911; texting info to all contacts'


@app.route("api/v1/update")
def updateCB():
	return "Endpoint for updating cb"



################### Actions #####################

def extract_and_sanitize_num():
	numArg = request.args.get('number')
	num = sanitize.sanitize_num(numArg)	
	if num == None:
		return None
	else:
		return num

def extract_and_sanitize_arg():
	msgArg = request.args.get('message')
	msg = sanitize.sanitize_msg(msgArg)
	if msg == None:
		return None
	else:
		return None

################### Start Server #####################

if __name__ == '__main__':
    app.debug = True
    app.run()
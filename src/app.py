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
	num, msg = extract_sanitize_911text()
	if num == None or msg == None:
		# send return text saying failed
	else:
		# forward msg to all contacts & 911
	pass


@app.route("api/v1/call911")
def call911():
	return 'Called 911; texting info to all contacts'


@app.route("api/v1/update")
def updateCB():
	return "Endpoint for updating cb"



################### Actions #####################

def extract_sanitize_911text():
	num = extract_sanitize_911text_num()
	msg = extract_sanitize_911text_msg()
	if num == None or msg == None:
		return None, None
	else:
		return num, msg

def extract_sanitize_911text_num():
	numArg = request.args.get('number')
	num = sanitize.sanitize_num(numArg)	
	if num == None:
		return None
	else:
		return num

def extract_sanitize_911text_msg():
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
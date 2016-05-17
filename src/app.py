import os
from flask import Flask
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)


# Find these values at https://twilio.com/user/account
account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = TwilioRestClient(account_sid, auth_token)


################### Routes #####################

@app.route("/")
	def root_page():
		return '360 Broadcast Backend Landing Page\n' + 'If you are a user, you should not be seeing this!'



################### Start Server #####################

if __name__ == '__main__':
    app.debug = True
    app.run()
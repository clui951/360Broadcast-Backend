### Receives and Sends Twilio Content ###\
import twilio.twiml
from twilio.rest import TwilioRestClient


################### Twilio Auth #####################
# Find these values at https://twilio.com/user/account
account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = TwilioRestClient(account_sid, auth_token)
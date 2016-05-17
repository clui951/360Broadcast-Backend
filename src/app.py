from flask import Flask

app = Flask(__name__)


################### Routes #####################

@app.route("/")
	def root_page():
		return '360 Broadcast Backend Landing Page\n' + 'If you are a user, you should not be seeing this!'



################### Start Server #####################

if __name__ == '__main__':
    app.debug = True
    app.run()
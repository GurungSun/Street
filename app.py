from flask import Flask,render_template, url_for
from arts import art

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html", arts=art)

if __name__ == "__main__": 
	app.run(debug=True, host = '0.0.0.0', port=5100)
from flask import Flask, flash, redirect, render_template, request, session, abort
import json, requests 
from config import accesstoken
app = Flask(__name__)
token=accesstoken().assign_token()

@app.route("/")
def login():
    return render_template('index.html')

@app.route("/take")
def home():
	r=requests.get("https://api.onedrive.com/v1.0/drive",
		headers = {'Content-Type': 'application/json'},
		params={'access_token':token})
	rstr= str(r.text)
	rjson=json.loads(rstr)
	return rjson['id']
if __name__ == "__main__":
    app.run(debug=True)

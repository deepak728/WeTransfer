from flask import Flask, flash, redirect, render_template, request, session, abort
import json, requests 
import mysql.connector
from config import accesstoken,dbconnect
app = Flask(__name__)
token=accesstoken().assign_token()
db_config=dbconnect().db_config()

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
	userdata = {
	    'driveid': rjson['id'],
  		'drivetype': rjson['driveType'],
  		'name': rjson['owner']['user']['displayName']
	}
	db = mysql.connector.connect(host=db_config['host'],database=db_config['database'],user=db_config['user'],password=db_config['password'])
	cursor = db.cursor()
	add_user = ("INSERT INTO user (driveid,drivetype,name) VALUES (%(driveid)s, %(drivetype)s, %(name)s)")
	cursor.execute(add_user, userdata)

	r=requests.get("https://api.onedrive.com/v1.0/drive/root:/share:/children",
		headers = {'Content-Type': 'application/json'},
		params={'access_token':token})
	rstr= str(r.text)
	rjson=json.loads(rstr)
	length=len(rjson['value'])
	for i in range(0,length):
		filedata={
			'driveid': rjson['value'][i]['createdBy']['user']['id'],
			'id':rjson['value'][i]['id'],
			'filename':rjson['value'][i]['name'],
			'size': rjson['value'][i]['size']
		}
		add_files = ("INSERT INTO files (driveid,id,filename,size) VALUES (%(driveid)s, %(id)s, %(filename)s, %(size)s)")
		cursor.execute(add_files, filedata)
	db.commit()
	cursor.close()
	db.close()
	return r.text
	

if __name__ == "__main__":
    app.run(debug=True)

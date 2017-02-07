from flask import Flask, flash, redirect, render_template, request, session, abort
import json, requests 
import mysql.connector
from config import dbconnect
import os
app = Flask(__name__)
db_config=dbconnect().db_config()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/callback")
def abc():
    return render_template('call.html')    

@app.route("/login")
def login():
	token = request.cookies.get('odauth')
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
		re=requests.get("https://api.onedrive.com/v1.0/drive/items/"+rjson['value'][i]['id']+"/thumbnails/0/large",
		headers = {'Content-Type': 'application/json'},	
		params={'access_token':token})
		restr= str(re.text)
		rejson=json.loads(restr)
		filedata={
			'driveid': rjson['value'][i]['createdBy']['user']['id'],
			'id':rjson['value'][i]['id'],
			'filename':rjson['value'][i]['name'],
			'size': 'Size:' + str(rjson['value'][i]['size']/1024)+'MB',
			'downloadurl':rjson['value'][i]['@content.downloadUrl'],
			'thumbnail':rejson['url']
		}

		add_files = ("INSERT INTO files (driveid,id,filename,size,downloadurl,thumbnail) VALUES (%(driveid)s, %(id)s, %(filename)s, %(size)s,%(downloadurl)s,%(thumbnail)s)")
		cursor.execute(add_files, filedata)
	db.commit()
	cursor.execute("SELECT * FROM files")
	data = cursor.fetchall()
	return render_template('home.html',data=data)
	
	
@app.route("/home")
def home():
	db = mysql.connector.connect(host=db_config['host'],database=db_config['database'],user=db_config['user'],password=db_config['password'])
	cursor = db.cursor()
	cursor.execute("SELECT * FROM files")
	data = cursor.fetchall()
	return render_template('home.html',data=data)


	

if __name__ == "__main__":
    app.run(debug=True)

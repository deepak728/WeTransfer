from flask import Flask, flash, redirect, render_template, request, session, abort
import json, requests 
app = Flask(__name__)
 
@app.route("/")
def login():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

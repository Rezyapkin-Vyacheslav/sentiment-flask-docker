from flask import Flask, request, jsonify, abort, redirect, url_for, render_template, send_file
from sklearn.externals import joblib
import numpy as np
import pandas as pd

from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired

from codecs import open
import time


app = Flask(__name__)

print ("Preparing classifier")
start_time = time.time()
clf = joblib.load('clf.pkl')
print ("Classifier is ready")
print (time.time() - start_time, "seconds")

@app.route('/')
def index():
    return "Hello, very Guy!!"

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
MAX_LEN = 10
@app.route("/sentiment-demo", methods=["POST", "GET"])
def index_page(text="", prediction_message=""):
    if request.method == "POST":
        text = request.form["text"]
        if len(text)< MAX_LEN:
            with open("ydf_demo_logs.txt", "a", "utf-8") as logfile:
                print(text)
                print ("<response>")
                prediction_message = "with proba={:.2} I suppose it is a good film".format(clf.predict_proba([text])[0][1])
                print(prediction_message)
                print ("</response>")
        else:
            prediction_message = 'Len of text must be less than 100000'
	
    return render_template('hello.html', text=text, prediction_message=prediction_message)

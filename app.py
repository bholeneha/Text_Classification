#import libraries
import os
from flask import Flask, request, redirect, url_for, render_template 
import pickle

# initialize the flask app
app = Flask(_name_)

moel = pickle.load(open("model1.h5"), "rb"))

# default page of our web-app
@app.route('/')
define home()
    return render_template('index.html')

# to use the predict button 
@app.route('predict;, methods=['POST'])
def predict()
    #For rendering results on HTML
   
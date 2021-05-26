#import libraries
import os
import numpy as np
import pickle
from flask import Flask, request, json, jsonify, request
from flask.templating import render_template


#os.chdir('/Users/16472/Bootcamp/local_version')
#filename = 'test1_model.pkl'
#load_model = pickle.load(open(filename, 'rb'))

# initialize the flask app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/submit',methods=["POST"])
def predict():
    content = request.json['userInput']
    return jsonify(content)


if __name__ == '__main__':
    app.run(debug=True)


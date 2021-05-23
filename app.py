#import libraries
import os
import numpy as np
import pickle
from flask import Flask, request, redirect, url_for, render_template 
#from __future__ import unicode_literals
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
from string import punctuation
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.externals import joblib
from sklearn.naive_bayes import MultinomialNB


os.chdir('/Users/16472/Bootcamp/local_version')
filename = 'test1_model.pkl'
load_model = pickle.load(open(filename, 'rb'))

# initialize the flask app
app = Flask(__name__)

cv = CountVectorizer()
clf = MultinomialNB()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods=["POST"])
def submit():
    pickle.dump(clf, 'test1_model.pkl')
    clf = pickle.load(load_model)

    if request.method == 'POST':
        message = request.form['text']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction1 = clf.predict(vect)

    return render_template('index.html', predictions_class1 = my_prediction1)

if __name__ == '__main__':
    app.run(debug=True)


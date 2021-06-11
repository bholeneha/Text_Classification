# load dependencies
import os
import numpy as np
from flask import Flask, request, json, jsonify, request, url_for
from flask.templating import render_template
from string import punctuation
import regex
import pandas as pd
import json
import joblib

import nltk
nltk.download()
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('wordnet')
from nltk.tokenize import WordPunctTokenizer
from nltk.stem import WordNetLemmatizer



import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


# load models
try:
    new_lda = gensim.models.LdaModel.load('model/lda.model')
except: 
    print("Could not load lda")
try:
    count_vect, tfidf_transformer, CLF_model = joblib.load('model/clf_model.model')
except:
    print("Could not load other dude")

# define variables for LDA model
wordnet_lemmatizer = WordNetLemmatizer()
stop = stopwords.words('english')

# required for LDA model
for punct in punctuation:
    stop.append(punct)

def filter_text(text, stop_words):
    word_tokens = WordPunctTokenizer().tokenize(text.lower())
    filtered_text = [regex.sub(u'\p{^Latin}', u'', w) for w in word_tokens if w.isalpha() and len(w) > 3]
    filtered_text = [wordnet_lemmatizer.lemmatize(w, pos="v") for w in filtered_text if not w in stop_words] 
    return " ".join(filtered_text)


# initialize the flask app
app = Flask(__name__)

# define app routes
# routes to index on start of flask
@app.route('/')
def home():
    return render_template('index.html')

# route used when user clicks link to classify using Naive Bayes model
@app.route('/prediction_page')
def prediction_page():
    return render_template('model_1.html')

# route used when user clicks link to classify using LDA model
@app.route('/predictions_two')
def predictions_two():
    return render_template('model_2.html')

# route used when home button is clicked on Naive Bayes model
@app.route('/home_page')
def home_page():
    return render_template('index.html')

# prediction for NB model
@app.route('/api/submit', methods=["POST"])
def predict():
    predict = request.json['userInput']
    prediction = CLF_model.predict(count_vect.transform([f"{predict}"]))
    return json.dumps(prediction.tolist())
    
# route used when user clicks link to classify using LDA model
@app.route('/api/lda',methods=["POST"])
def predict_two():
    content = request.json['userInput']
    filteredContent = filter_text(content, stop)
    word_list = []
    temp = filteredContent.split(" ")
    word_list.append(temp)
    id2word = corpora.Dictionary(word_list)
    texts = word_list
    corpus = [id2word.doc2bow(text) for text in texts]
    unseen_doc = corpus
    classification = list(new_lda.get_document_topics(unseen_doc))
    result = ""
    for x in classification[0]:
        topic = x[0]
        prob = x[1]
        result+=(f"{topic} {prob},")
    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True)
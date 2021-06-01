# load dependencies
import os
import numpy as np
from flask import Flask, request, json, jsonify, request
from flask.templating import render_template
import nltk
from nltk.corpus import stopwords
import gensim.corpora as corpora
from string import punctuation
import regex
import numpy as np 
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import regex
from nltk.corpus import stopwords 
from nltk.tokenize import WordPunctTokenizer
from string import punctuation
from nltk.stem import WordNetLemmatizer
import nltk
from wordcloud import WordCloud
import gensim
import json
from gensim.utils import simple_preprocess
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# load models
os.chdir('/Users/16472/Bootcamp/text_classification-')
new_lda = gensim.models.LdaModel.load('model/lda.model')
count_vect, tfidf_transformer, CLF_model = joblib.load('model/clf_model.model')

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
    result = []
    for x in classification[0]:
        temp = {}
        temp["topic"] = x[0]
        temp["prob"] = x[1]
        result.append(temp)
    return json.dumps(str(result))

if __name__ == '__main__':
    app.run(debug=True)
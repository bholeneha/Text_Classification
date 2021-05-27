#import libraries
import os
import numpy as np
import pickle
from flask import Flask, request, json, jsonify, request
from flask.templating import render_template
import nltk
#nltk.download('stopwords')
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
#from wordcloud import WordCloud
from nltk.corpus import stopwords 
from nltk.tokenize import WordPunctTokenizer
from string import punctuation
from nltk.stem import WordNetLemmatizer
import nltk
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')



wordnet_lemmatizer = WordNetLemmatizer()

stop = stopwords.words('english')

for punct in punctuation:
    stop.append(punct)

def filter_text(text, stop_words):
    word_tokens = WordPunctTokenizer().tokenize(text.lower())
    filtered_text = [regex.sub(u'\p{^Latin}', u'', w) for w in word_tokens if w.isalpha() and len(w) > 3]
    filtered_text = [wordnet_lemmatizer.lemmatize(w, pos="v") for w in filtered_text if not w in stop_words] 
    return " ".join(filtered_text)



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
    filteredContent = filter_text(content, stop)
    word_list = []
    temp = filteredContent.split(" ")
    word_list.append(temp)
    id2word = corpora.Dictionary(word_list)
    texts = word_list
    corpus = [id2word.doc2bow(text) for text in texts]
    return jsonify(corpus)



if __name__ == '__main__':
    app.run(debug=True)


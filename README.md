# Text Classification

## Problem to Solve
Perform text classification on email data and categorize data into four categaries; crime, politics, entertainment and science. This problem falls under "Topic Modelling".

## Rationale for Topic 
Text classification has wide variety of applications in various domains. It can be used in cyber security for classification of documents on the basis of privacy and confidentiality. It can be used for sentiment analysis for customer reviews in on line shopping etc. 

## Team Members
* Fatima Hussain- Model development and technology selection
* Neha - Data Cleaning
* Bev - Dashboard 
* Veronika - Database
* Sibtain - GitHub

### Communication protocol:
- Slack group
- Zoom 
- Meetings 4 times per week 

## Machine Learning Model 
We intend to perform text classification and use Latent Dirichlet Allocation algorithm.
It is an exploratory process and LDA identifies the hidden topic structures in text documents.  It uses Bayesian statistics and Dirichlet distributions for processing and identifying the topics.

We may consider using the following classification algorithm, along with LDA:
* KNN
* Logistic Regression

### Data Preprocessing
Prior to text classification,  LDA pre-process the raw text/document.

* Normalization: Transform text to normal/canonical form
* Stemming: Reduce a word to its word stem/root without suffixes and prefixes 
* Stopwordremoval: Remove words that do not add any logical meaning 
* Lemmatization:  Words in third person are changed to first person and verbs in past and future tenses are changed into present.
* Tokenization: Break text into ‘tokens’, i.e. words and phrases. Split the text into sentences and the sentences into words. Lowercase the words and remove punctuation.

# Segment 2

## Machine Learning Model 
We performed data cleaning before applying LDA model, and performed following steps:
### Data Preprocessing
*  Raw data was available in txt files and we created  data frame for all the data and stored in the google COLAB.
*  Stop words are removed and data is lemanized and tokanized. imported "stopwords" from nltk.corpus ,  "WordPunctTokenizer" from nltk.tokanize, "punctuation" from string, and WordNetLemmatizer from nltk.stem 
* Cleaned data is stored in the same dataframe with column name "Filtered Text"

### Bag of Words
Before applying the LDA model, we developed the "Bag of Words" from the "Filtered Text" column:

* Entire sentence is split on spaces and words are separated.
* Dictionary of words is created by  importing  "gensim" and "simple_preprocess" from gensim.utils
* Each word will be shown by no. of times, it appears in the dictionary

### LDA Model Details: 
* We used: lda_model = gensim.models.LdaMulticore(corpus=corpus, id2word=id2word,num_topics=num_topics) to build the model and tried with different number of topics. 
* We see distinct clusters when we choose "No. Topics=4".  If "No. Topics" are increases, intersecting clusters are formed, clearly showing that data set has distinct four categories of text.
* We used pyLDAvis.gensim to see the visuals.

### Datasets 

* [NIPS Papers Dataset](https://github.com/kapadias/mediumposts/blob/master/natural_language_processing/topic_modeling/data/NIPS%20Papers.zip)
* [Emails Dataset](https://www.kaggle.com/dipankarsrirag/topic-modelling-on-emails)

We intend to use one or both of these datasets. 

![Four distinct topic](Images/four.png)
![Overlapping Clusters](Images/eight.png)

## Database
Since the dataset used in this project is unstructured therefore Amazon S3 is more appropriate than a conventional SQL database. 

## Dashboard
Technology 
- HTML webpage using Flask
- CSS stylepage
- Bootstrap 4
- JS (ES11) 
- consider the use of Tableau 
Layout
- consideration to be given on how to be included in final presentation....

## Clustering PM Job Descriptions
# We use K-Means and Agglomerative Clustering for clustering analysis. 
# To better understand overarching similarities 

import pandas as pd
from sklearn.cluster import KMeans
import nltk
nltk.download('punkt') 
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger') 

import gensim
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

jd = pd.read_csv('jds.csv')

desc = jd.iloc[:,2]
desc_list = desc.values.tolist()

qual = jd.iloc[:,3]
qual_list = qual.values.tolist()

# Analyzing listing description (desc_list) first

# 1. Tokenize, 2. Lemmatize, 3. Remove stop words and punctuation

processed_desc = []

for x in processed_desc:
    token = nltk.word_tokenize(x)
    lemmatizer = nltk.stem.WordNetLemmatizer()
    lemmatized_token = [lemmatizer.lemmatize(x) for x in token if x.isalpha()]
    stop_words_removed = [x for x in lemmatized_token if not x in stopwords.words('english') if x.isalpha()]
    processed_desc.append(stop_words_removed)

#processed_desc
processed_desc2 = list(map(' '.join, processed_desc))
print(processed_desc2)

# Analysing listing qualifications (qual_list) second
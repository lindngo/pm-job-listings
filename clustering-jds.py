## Clustering PM Job Descriptions
# K-Means and Agglomerative Clustering will be used to understand similarities across the collected job descriptions. 

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings
warnings.filterwarnings("ignore")

jd = pd.read_csv('jds.csv')

# Creating two lists to hold the job descriptions and their respective qualifications. 

desc = jd.iloc[:,2]
desc_list = desc.values.tolist()

qual = jd.iloc[:,3]
qual_list = qual.values.tolist()

# 1. Analyzing job description (desc_list) 
vectorizer1 = TfidfVectorizer(stop_words = 'english')
X1 = vectorizer1.fit_transform(desc_list)

# 1a. Choosing number of clusters
model1 = KMeans(n_clusters = 6)
model1.fit(X1)
print(model1.cluster_centers_)

model1.fit_transform(X1)
model1_clusters = model1.labels_.tolist()
print(model1_clusters)

# 1b. Finding the characteristics for each cluster
centroids = model1.cluster_centers_.argsort()[:,::-1]
terms = vectorizer1.get_feature_names_out()

for c in range(6):
    print('Cluster%d:' % c)

    for ind in centroids[c, :6]:
        print(terms[ind])

# 2. Analzying qualifications (qual_list)
vectorizer2 = TfidfVectorizer(stop_words = 'english')
X2 = vectorizer2.fit_transform(qual_list)

# 2a. Choosing number of clusters
model2 = KMeans(n_clusters = 6)
model2.fit(X2)
print(model2.cluster_centers_)

model2.fit_transform(X2)
model2_clusters = model2.labels_.tolist()
print(model2_clusters)

# 2b. Finding the characteristics for each cluster
centroids2 = model2.cluster_centers_.argsort()[:,::-1]
terms = vectorizer2.get_feature_names_out()

for c in range(6):
    print('Cluster%d:' % c)

    for ind in centroids2[c, :6]:
        print(terms[ind])
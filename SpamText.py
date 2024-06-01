# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

# loading data set
df = pd.read_csv("SPAM text message 20170820 - Data.csv")
# print(df.head())

# set ham and spam into 0 and 1
df["Category"].replace({"spam": 1, "ham": 0}, inplace=True)

# gain insight from data
data = {'Category': ['spam', 'ham'], 'number': [len(df.loc[df['Category'] == 1]), len(df.loc[df['Category'] == 0])]}
df_count = pd.DataFrame(data, columns=['Category', 'number'])
# print(df_count.head())

# show the chart of the data with matplotlib
df_count.plot(x='Category', y='number', kind='bar')
# plt.show()

# now lets cleaning the data
stemmer = PorterStemmer()
corpus = []

for word in range(len(df['Message'])):
    msg = df['Message'][word]
    msg = re.sub('[^a-zA-Z]', ' ', msg)
    msg = msg.lower()
    msg = msg.split()
    msg = [stemmer.stem(word) for word in msg if not word in set(stopwords.words('english'))]
    msg = ' '.join(msg)
    corpus.append(msg)


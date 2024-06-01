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
df["Category"].replace({1: "spam", 0: "ham"}, inplace=True)

# gain insight from data
data = {'Category': ['spam', 'ham'], 'number': [len(df.loc[df['Category'] == 1]), len(df.loc[df['Category'] == 0])]}
df_count = pd.DataFrame(data, columns=['Category', 'number'])
print(df_count.head())
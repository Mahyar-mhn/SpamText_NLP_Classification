# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

# loading data set
df = pd.read_csv("SPAM text message 20170820 - Data.csv")
print(df.head())

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from apyori import apriori

#here import the data
dataset=pd.read_csv('data.csv',header=None)
records=[] for i in range(0,101):
 records.append([str(dataset.values[i,j])for j in range (0,10)])

#here train the model
rules=apriori(records,min_support=0.1,min_confidence=0.2,min_lift=3,min_length=2)

results=list(rules)
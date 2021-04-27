import numpy as np
import pandas as pd

## import dataset
dataset = pd.read_csv("Batchelor_Degree_Categories.csv")
##use indexing to find how many and which courses are in 10th position
x = dataset.Subject[10]
print(x)
y = dataset.Courses[10]
print(y)
## use indexing to show first 10 records
s = dataset
print(s[:10])



import numpy as np
import pandas as pd

dataset = pd.read_csv("Batchelor_degrees2017_18.csv")


#find the missing values
print(dataset.isnull().sum())

#replace missing values
cleaned_data = dataset.fillna(method='bfill', axis=0).fillna(0)
print(cleaned_data.isnull().sum())
print(dataset.shape)

#drop duplicate rows
drop_duplicates= dataset.drop_duplicates()
print(dataset.shape, drop_duplicates.shape)












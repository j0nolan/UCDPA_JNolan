import numpy as np
import pandas as pd

dataset = pd.read_csv("baseball.csv")

##look at dataset shape
print(dataset.shape)

#print first 5 rows
print(dataset.head())

##show dataset columns
print(dataset.columns)

#group by position
print(dataset.groupby("Position").count())

##sort by  number of seasons
print(dataset.Number_seasons.sort_values)

#slicing using the numer of seasons column
x = dataset.Number_seasons[:12]
print(x)

#use loc to display player names Triples, and home runs
print(dataset.loc[0:3, ["Player", "Triples", "Home_runs"]])

#use iloc to display the first 5 rows and 7th to 10th columns
print(dataset.iloc[0:5, 6:11])









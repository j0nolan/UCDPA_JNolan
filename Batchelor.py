import os
import pandas as pd
print(os.getcwd())

# import datasets
dataset1 = pd.read_csv("Batchelor_degrees2017_18.csv")
dataset2 = pd.read_csv("Batchelor_Degree_Categories.csv")

# merge datasets on left in a many to one join to keep all records
left_dataset = pd.merge(dataset1, dataset2, on="Subject", how="left")
print(left_dataset)
print(dataset1.shape, dataset2.shape)
print(left_dataset.shape)

# look at dataset2 prior to plotting
print(dataset2.head())
print(dataset2.columns)

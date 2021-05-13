import pandas as pd

# import dataset
dataset = pd.read_csv("baseball.csv")

# print first 5 rows
print(dataset.head())

# trial for loop
for lab in dataset.iterrows():
    print(lab)

# length of table
print(len(dataset))
# length of "Player" column as possible primary key
print(len(dataset.Player.unique()))

# shape of dataset
print(dataset.shape)

# columns in table
print(dataset.columns)

# datatypes in dataset
print(dataset.info())

# get rid of duplicates
drop_duplicates = dataset.drop_duplicates(subset=["Player"])
print(dataset.shape, drop_duplicates.shape)

# count missing values
missing_values_count = dataset.isnull().sum()
print(missing_values_count)

# how many instances of players in hall of fame
print(dataset['Hall_of_Fame'].value_counts())

# Players who have more than one "Hall of Fame" event
print(dataset[dataset["Hall_of_Fame"] >1])

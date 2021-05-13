import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.use('tkagg')

import matplotlib.pyplot as plt

# import dataset for visualising
dataset2 = pd.read_csv("Batchelor_Degree_Categories.csv")

# look at dataset2 prior to plotting
print(dataset2.head())
print(dataset2.columns)

# drop the first row containing the "all fields total"
dataset2.drop(index=dataset2.index[0],
              axis=0,
              inplace=True)
print(dataset2.head())

# select columns to be plotted
x = dataset2["Subject"]
y1 = dataset2["Courses"]
y2 = dataset2["Total"]
y3 = dataset2["Males"]
y4 = dataset2["Females"]

# plot x and y1
plt.plot(x,y1)
plt.xlabel("Subject")
plt.ylabel("No of Courses")
plt.show()

# plot x and y2
plt.plot(x,y1)
plt.xlabel("Subject")
plt.ylabel("Total Number of Students")
plt.show()

# plot x and y3
plt.plot(x,y3)
plt.xlabel("Subject")
plt.ylabel("Number of Male Students")
plt.show()

# plot x and y4
plt.plot(x,y4)
plt.xlabel("Subject")
plt.ylabel("Number of Female Students")
plt.show()

# plot x and y3 and y4 together
plt.plot(x,y3, color ="#0000cd")
plt.plot(x,y4, color = "#ff0000")
plt.xlabel("Subject by Gender Blue = Male, Red = Female")
plt.show()


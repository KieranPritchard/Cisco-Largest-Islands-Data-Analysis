import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reads in the data from the largest islands file
islands = pd.read_csv('./largest-islands.csv')

# Sorts the files based on area and ascending
islands = islands.sort_values(by="area", ascending=False)

# Extracts the first ten islands
islands = islands.head(10)

# Extracts the islands and stores them
island_list = islands["island"]

# Extracts the area and stores them
area = islands["area"]

# Plots the x and y values
x = np.array(island_list)
y = np.array(area)

# Outputs a bar chart
plt.barh(x, y)
plt.show()
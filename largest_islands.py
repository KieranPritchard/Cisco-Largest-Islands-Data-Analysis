import pandas as pd

# Reads in the data from the largest islands file
islands = pd.read_csv('./largest-islands.csv')

# Sorts the files based on area and ascending
islands = islands.sort_values(by="area", ascending=True)

# Extracts the islands and stores them
island_list = islands["island"]

# Extracts the area and stores them
area = islands["area"]
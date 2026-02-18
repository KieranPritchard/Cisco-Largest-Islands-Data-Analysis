import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reads in the data
islands = pd.read_csv('./largest-islands.csv')

# Sorts and grabs top 10
# Note: ascending=True makes the largest island appear at the TOP for barh
islands = islands.sort_values(by="area", ascending=True).tail(10)

# Extracts the data
island_list = islands["island"]
area = islands["area"]

# Making height 4 makes the chart significantly shorter/flatter
plt.figure(figsize=(10, 4))

# Plots with styling
plt.barh(island_list, area, color='teal', edgecolor='black')

# Styling the title and labels
plt.title("Top 10 Islands by Area", fontsize=14, fontweight='bold')
plt.xlabel("Area (sq km)", fontsize=10)
plt.ylabel("Island", fontsize=10)

# Adds a light grid for readability
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Ensures everything fits within the new smaller aspect ratio
plt.tight_layout()

# bbox_inches='tight' ensures the saved PNG matches the cropped aspect ratio
plt.savefig('top_10_islands_by_area_small.png', dpi=300, bbox_inches='tight')

# Outputs the bar chart
plt.show()
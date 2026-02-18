# Cisco-Largest-Islands-Data-Analysis

## Project Description

### Objective

To build a data visualization tool using Pandas and Matplotlib that analyzes the world's largest islands. This project focuses on cleaning, sorting, and presenting geographical data in a clear, professional horizontal bar chart.

### Features

* Automated data ingestion from CSV files.
* Dynamic sorting to identify the top 10 largest landmasses.
* Customized horizontal bar charts for better readability of long island names.
* Automatic high-resolution export to PNG format.

### Technologies and Tools Used

* **Language:** Python
* **Frameworks/Libraries:** pandas, matplotlib, numpy
* **Tools:** Git, GitHub, VS Code

### Challenges Faced

One significant challenge was managing the Matplotlib "buffer" — specifically, I found that calling plt.show() before plt.savefig() resulted in blank images because the figure clears itself after displaying. I also had to experiment with the aspect ratio using figsize to ensure the chart didn't look too stretched or cramped when dealing with ten different data points.

### Outcome

Successfully created a script that transforms raw CSV data into a polished, "panoramic" style visual. This built my confidence in using Pandas for data manipulation and understanding the finer styling details of Matplotlib.

## How to Use the Project

1. **Setup**

* Ensure you have your data file named largest-islands.csv in the same directory as your script.

2. **Install Dependencies**

* Make sure you have the necessary libraries installed:

```Bash
pip install pandas matplotlib numpy
```

3. **Run the Analysis**

* Open your terminal or IDE.

* Run the script:

```Bash
python island_viz.py
```

4. **Output**

* The program will generate a window displaying the bar chart.

* A high-resolution file named top_10_islands_by_area.png will be saved to your project folder.

## License

This project is licensed under the [MIT License](LICENSE).


# Data Source:

Ghosh, Iman. "Visualizing the World’s 100 Biggest Islands." Visual Capitalist, Visual Capitalist, 19 Aug. 2021, www.visualcapitalist.com/visualizing-100-worlds-biggest-islands/.

Based upon a map by David Garcia. 

Island areas from Britannica and Wikipedia.

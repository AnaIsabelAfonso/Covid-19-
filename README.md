# 📊 COVID‑19 Data Analysis  
Project for the **Applied Programming** course – University

## 📌 Project Overview
This project performs an exploratory and statistical analysis of global COVID‑19 data using Python.  
It demonstrates data acquisition, cleaning, transformation, visualization, and basic modeling techniques.

The workflow includes:

- Importing real COVID‑19 datasets from Johns Hopkins University  
- Reshaping and indexing time‑series data  
- Aggregating results by country  
- Combining epidemiological data with population statistics  
- Creating visualizations  
- Fitting a polynomial model  
- Computing normalized metrics such as *cases per million inhabitants*

## 🛠️ Technologies Used
- Python 3  
- NumPy  
- Pandas  
- Matplotlib
- 

## 📂 Project Structure

### **1. Data Import**
The script loads three datasets directly from the Johns Hopkins University GitHub repository:

- Confirmed cases  
- Deaths  
- Recovered cases  

Each dataset is printed for initial inspection.

### **2. Data Transformation**
Three functions (`indexar1`, `indexar2`, `indexar3`) convert the wide-format time‑series into long-format tables using:

- `pandas.melt()`  
- Multi‑indexing by Province/State, Country/Region, and Date  

This prepares the data for grouping and merging.

### **3. Aggregation by Country**
The script groups each dataset by country and extracts the most recent available values.

### **4. Dataset Consolidation**
A final table is created by joining:

- Confirmed cases  
- Deaths  
- Recovered cases  

A new metric is computed: Active Cases = Confirmed − Deaths

### **5. Sorting**
Countries are sorted by the number of active cases.

### **6. Integration with Population Data**
A local file `Pop.csv` is imported to include population values.

The script:

- Identifies countries common to both datasets  
- Filters and aligns population data  
- Cleans population values (removing spaces, converting to integers)  
- Merges population with the COVID‑19 dataset  

### **7. Visualization**
A scatter plot is generated comparing:

- Confirmed cases  
- Deaths  

for the 15 countries with the lowest number of active cases.

### **8. Polynomial Regression**
A second‑degree polynomial is fitted to the scatter data using NumPy: p = np.poly1d(np.polyfit(x, y, deg=2))


The fitted curve is plotted alongside the data points.

### **9. Data Cleaning**
Population values are converted to integers after removing formatting inconsistencies.


### **10–11. Normalized Metrics**
The script computes:

- **Confirmed cases per million inhabitants**
- **Deaths per million inhabitants**

These metrics allow fair comparison between countries of different sizes.



## 📈 Outputs
The program produces:

- A consolidated table with epidemiological and population data  
- Scatter plots and polynomial regression curves  
- Rankings of countries by active cases  
- Normalized indicators (cases per million)  


## ▶️ How to Run
1. Install required libraries:

   pip install numpy pandas matplotlib
   
2. Place Pop.csv in the same directory as the script.
   
3. Run the Python file:
   python Project Covid-19.py





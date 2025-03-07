Project Overview
This project is a comprehensive data analysis tool developed in Python, designed to help users analyze and visualize data effectively. 
The project includes various functionalities such as creating charts (pie charts, bar graphs, line graphs, scatter plots), calculating 
statistical measures, recording and managing sales data, and forecasting sales. The program is built using Python libraries such as matplotlib, 
mysql.connector, statistics, and PySimpleGUI for graphical user interface (GUI) development.

Features
Data Visualization:
  Pie Chart: Create pie charts to visualize data distribution.
  Bar Graph: Generate bar graphs to compare different categories.
  Line Graph: Plot line graphs to show trends over time.
  Scatter Plot: Create scatter plots to visualize relationships between variables.
Statistical Analysis: 
  Calculate mean, median, mode, standard deviation, and variance for a given dataset.
  Display minimum and maximum values in the dataset.
Sales Management:
  Record sales data (product name, quantity, price, sale date).
  Display, search, add, delete, and update sales records.
Sales Forecasting:
  Forecast sales based on initial product count and observed sales increment.

Prerequisites
Before running the program, ensure you have the following installed:
  Python 3.x
  MySQL Server (for database operations)

Required Python libraries:
  matplotlib
  mysql.connector
  statistics
  PySimpleGUI

Running the Program
  1. Clone the repository or download the project files.
  2. Set up the database as described above.
  3. Run the Python script:
    python data_analysis.py
  4. Main Menu: The program will display a GUI with the following options:
        Create Pie Chart
        Display Bar Graph
        Display Line Graph
        Get Statistics
        Record Sales
        Create Scatter Point Graph
        Forecast or Calculate your Sales
        Exit

Usage Instructions
 1. Pie Chart:
      Enter the title, labels, and sizes for the pie chart.
      The chart will be displayed, and the data will be saved in the chart_info table.
 2. Bar Graph:
      Enter the title, labels, and sizes for the bar graph.
      The graph will be displayed, and the data will be saved in the chart_info table.
 3. Line Graph:
      Enter the title and the number of data points.
      Input the x and y values for each data point.
      The line graph will be displayed.
 4. Get Statistics:
      Enter the number of data points.
      Input the values for each data point.
      The program will calculate and display the mean, median, mode, standard deviation, variance, minimum, and maximum values.
 5. Record Sales:
      Choose from options to create, display, search, add, delete, or update sales records.
      Sales data will be stored in the sales table.
 6. Scatter Point Graph:
      Enter the number of data points.
      Input the x and y values for each data point.
      The scatter plot will be displayed.
 7. Sales Forecast:
      Enter the starting number of products and the observed sales increment.
      The program will calculate and display the total sales for a specified date range.
    
Advantages of Data Analysis
  Improved Decision Making: Data analysis helps in making informed decisions based on data-driven insights.
  Increased Efficiency and Productivity: Automating data analysis processes saves time and resources.
  Enhanced Customer Experience: Understanding customer behavior through data analysis can improve customer satisfaction.
  Improved Risk Management: Data analysis helps in identifying and mitigating risks.
  Competitive Advantage: Leveraging data analysis can provide a competitive edge in the market.

Limitations and Future Scope
  Limitations:
    1. Data Quality: The accuracy of the analysis depends on the quality of the data.
    2. Sample Size: Small sample sizes may lead to less reliable results.
    3. Methods: The choice of analysis methods can impact the results.
    4. Assumptions: Data analysis often relies on certain assumptions that may not always hold true.
    5. Interpretation: Misinterpretation of data can lead to incorrect conclusions.

  Future Scope:
    The scope of data analysis is expected to grow with advancements in technology and the availability of more data.
    The demand for skilled data analysts is expected to increase, with the Indian data analytics market projected to create over 11 million jobs by 2026.

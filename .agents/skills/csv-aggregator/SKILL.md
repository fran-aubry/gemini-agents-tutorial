---
name: csv-aggregator
description: Use this skill when asked to aggregate data from a CSV file and plot the results.
---
# CSV Analysis Workflow
When performing data analysis on a CSV file:

1. **Inspection**: Identify the available columns by reading the CSV header.
2. **Aggregation**: Load the data using `pandas`. Group the data by the specified column and perform a sum operation on the numerical target column.
3. **Visualization**: Create a plot (e.g., bar or pie chart) based on the aggregated data.
4. **Output**: Save the resulting plot to the current directory as a PNG file.
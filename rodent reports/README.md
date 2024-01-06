# Rodent Reports Visualization - Python Assignment

This Python script analyzes rodent reports data from a given file. The program reads a file containing rodent reports with neighborhood names, latitudes, and longitudes. It then performs the following actions:

## Functionality:
- **Reading Data:** Reads the file and extracts information about neighborhoods, latitudes, and longitudes of rodent reports.
- **Plotting Coordinates:** Plots the coordinates of rodent reports on a scatter plot relative to Northeastern University's location.
- **Bar Graph:** Generates a bar graph showing the number of rodent reports per neighborhood.
- **Calculations:** Calculates the total number of rodent reports, unique neighborhoods, and average reports per neighborhood.

## Usage:
1. **File Input:** Ensure the specified CSV file ('rodents_311_2021.csv') is available in the same directory.
2. **Run the Script:** Execute the Python script 'rodent_reports.py'.
3. **Output:** The script generates visualizations (scatter plot and bar graph) as PDF files.

## Output Files Generated:
- **boston_rodents.pdf: Scatter plot of rodent reports relative to Northeastern University.
- **neighborhoods.pdf: Bar graph displaying rodent report counts per neighborhood.

## File Structure:
- **rodent_reports.py: Python script containing code for data analysis and visualization.
- **README.md: Explanation of the script's functionality, usage instructions, and output description.
- **rodents_311_2021.csv: Data file containing rodent reports with neighborhood details.

# Exoplanets Analysis Assignment

This Python script aims to determine the planet most similar to Earth by analyzing a dataset of exoplanets. It employs several functions to calculate the Euclidean distance between planets, generate reports, and visualize data through scatter plots.

## Functionality:
1. **`read_data(file)`:** Reads and organizes the dataset into a 2D list of planet attributes.
2. **`lookup_planet(planet, data)`:** Extracts attributes of a specific planet from the dataset.
3. **`euclidean_distance(planet1_data, planet2_data)`:** Calculates the Euclidean distance between two planets.
4. **`find_most_similar_planet(planet_name, dataset)`:** Identifies the planet most similar to a given planet.
5. **`generate_planet_report(read_planet, from_data)`:** Generates a readable report of a desired planet.
6. **`extract_column(data, column_index)`:** Extracts a specific column from the dataset.
7. **`visualize_exoplanets(x_axis, y_axis, our_data, x_label, y_label)`:** Creates scatter plots of mass vs. semimajor axis and plots Earth's data.

## Usage:
1. **File Input:** Ensure the specified CSV file ('exoplanets.csv') is available in the same directory.
2. **Run the Script:** Execute the Python script 'exoplanet.py'.
3. **Output:** The script generates a scatter plot along with data for the planet that is most like Earth.

## Output Files Generated:
- **exoplanet.png: Scatter plot of mass vs. semimajor axis of planets with Earth highlighted.

## File Structure:
- **exoplanet.py: Python script containing code for data analysis and visualization.
- **README.md: Explanation of the script's functionality, usage instructions, and output description.
- **exoplanets.csv: Data file containing charactersitics of all discovered extra-solar planets.

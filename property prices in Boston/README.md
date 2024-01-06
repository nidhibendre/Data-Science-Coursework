# Housing Price Prediction

This repository contains code for a housing price prediction assignment that focuses on analyzing a dataset of houses in the Boston area and building models to predict housing prices based on various features.

## Functionality:
- **Part 1: Decision Tree Classifier**
  - Building a decision tree classifier to estimate the price bucket of housing based on features like beds, baths, area, and distance.
  - Visualizing the decision tree using `plot_tree()` and validating its behavior.

- **Part 2: Random Forest Classification**
  - Evaluating a Random Forest Classifier's performance using 10-fold cross-validation.
  - Constructing a confusion matrix and computing accuracy scores.

- **Part 3: Feature Importance in Random Forest**
  - Plotting feature importances using a RandomForestClassifier to understand which features contribute most to predicting price buckets.

- **Part 4: RandomForestRegressor and housing prices**
  - Employing a RandomForestRegressor to predict the actual housing price.
  - Evaluating the model's performance and plotting feature importances for regression.

- **Part 5: Ethics of Housing Pricing**
  - Discussing ethical considerations in using models to predict housing prices, particularly focusing on the potential impacts of biased models on racism, socioeconomic immobility, and social segregation.

## Usage:
To replicate or explore this assignment:
1. Clone this repository.
2. Ensure Python and necessary libraries are installed.
3. Run the code cells in the `housing_prediction.ipynb` notebook to replicate the analyses and visualize results.

## File Structure:
- `housing_prediction.ipynb`: Jupyter notebook containing Python code and analysis for the assignment.
- `boston_houses.csv`: Dataset used for the analysis.
- `README.md`: This file providing an overview of the assignment and repository structure.

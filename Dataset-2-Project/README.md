# Tip Amount Prediction using Linear Regression

## Overview

This project uses Linear Regression to predict the tip amount based on the bill amount. The dataset was loaded from an Excel file and prepared for machine learning model development.

## Tasks Performed

### Data Loading

* Loaded the dataset using Pandas
* Read data from an Excel file

### Data Preprocessing

* Removed the `Meal` column as it was not required for prediction
* Prepared the dataset for modeling

### Data Analysis

* Generated a correlation matrix to understand the relationship between variables

### Feature and Target Selection

* Selected bill amount as the feature (X)
* Selected observed tip amount as the target (y)

### Model Development

* Split the dataset into training and testing sets
* Built a Linear Regression model using Scikit-learn
* Trained the model on the training data

### Model Evaluation

* Predicted values on the test dataset
* Evaluated model performance using:

  * Mean Squared Error (MSE)
  * R² Score

### Prediction

* Predicted the expected tip amount for a $50 bill

## Libraries Used

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

## Machine Learning Technique

* Simple Linear Regression

# Day 4 – Customer Segmentation using K-Means Clustering

## Project Overview

This project explores Unsupervised Machine Learning using the K-Means Clustering algorithm. The goal is to segment mall customers into different groups based on their demographic information and spending behavior.

## Dataset

Mall Customers Dataset containing:

- CustomerID
- Genre (Gender)
- Age
- Annual Income (k$)
- Spending Score (1-100)

## Tasks Completed

### Data Exploration
- Loaded and inspected the dataset.
- Checked for missing values.

### Outlier Analysis
- Visualized Age and Annual Income using boxplots.
- Calculated Quartiles and Interquartile Range (IQR).
- Identified potential outliers.

### Data Preprocessing
- Applied Label Encoding to the Genre column.
- Removed CustomerID from model features.

### K-Means Clustering
- Implemented K-Means clustering.
- Used the Elbow Method to determine the optimal number of clusters.
- Calculated WCSS values.

### Visualization
- Visualized customer clusters using:
  - Annual Income
  - Spending Score

### Cluster Prediction
- Built a function to predict the cluster of a new customer based on:
  - Gender
  - Age
  - Annual Income
  - Spending Score

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Learning Outcomes

- Understanding Unsupervised Learning
- Customer Segmentation
- K-Means Clustering
- Elbow Method
- Outlier Detection
- Label Encoding
- Data Visualization

## Future Improvements

- Feature Scaling before clustering
- Silhouette Score Evaluation
- Interactive Cluster Dashboard
- Streamlit-based Customer Segmentation App
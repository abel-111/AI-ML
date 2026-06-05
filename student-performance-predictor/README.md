# 🎓 Student Performance Prediction using Machine Learning

## 📌 Project Overview

This project predicts a student's exam score based on academic and lifestyle factors such as study hours, attendance, previous scores, and sleep hours. A Random Forest Regression model is trained and optimized using GridSearchCV to improve prediction accuracy.

The project also integrates Generative AI to provide personalized study recommendations based on the predicted exam score.

---
## ▶️ Execution Environment

This project was developed and executed in **Google Colab**.

To run the project:

1. Open the notebook in Google Colab.
2. Upload the dataset file.
3. Add your own Gemini API key and ngrok token.
4. Run all cells in sequence.

**Note:** API keys and tokens are intentionally excluded from this repository for security reasons.

## 🎯 Objectives

- Analyze factors affecting student performance.
- Perform data preprocessing and feature engineering.
- Build a machine learning model to predict exam scores.
- Optimize model performance using hyperparameter tuning.
- Generate AI-powered study recommendations.
- Prepare the project for deployment using Streamlit.

---

## 📊 Dataset Features

The dataset includes factors such as:

- Hours Studied
- Attendance
- Previous Scores
- Sleep Hours
- Parental Involvement
- Access to Resources
- Motivation Level
- Family Income
- Teacher Quality
- School Type
- Peer Influence
- Internet Access
- Learning Disabilities
- Gender
- Exam Score (Target)

---

## 🛠️ Data Preprocessing

The following preprocessing techniques were applied:

- Handling missing values using mode imputation.
- Label Encoding for categorical features.
- Binary encoding for Yes/No attributes.
- Correlation analysis and visualization.
- Feature selection for model training.

---

## 📈 Exploratory Data Analysis

EDA was performed using:

- Box Plots
- Histograms
- Correlation Heatmaps

These visualizations helped identify patterns and relationships within the dataset.

---

## 🤖 Machine Learning Model

### Algorithm Used
- Random Forest Regressor

### Model Evaluation
- Train-Test Split
- Cross Validation
- R² Score

### Hyperparameter Tuning
- GridSearchCV

Parameters tuned:
- n_estimators
- max_depth
- min_samples_split

---

## 💾 Model Saving

The trained model is saved using Joblib, allowing it to be reused without retraining.

---

## 🧠 AI Study Coach

The project integrates Google's Gemini API to generate:

- Personalized Study Plans
- Daily Study Schedules
- Revision Strategies
- Time Management Tips
- Exam Preparation Guidance

based on the student's predicted performance.

---

## 🚀 Future Enhancements

- Complete Streamlit web application.
- Deploy the project online.
- Add more predictive features.
- Compare multiple regression models.
- Improve model performance through feature engineering.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Google Gemini API
- Streamlit
- Pyngrok

---

## 📂 Project Structure

student-performance-prediction/

├── student_performance_prediction.py

├── student_model.pkl

├── StudentPerformanceFactors.csv

├── README.md

└── requirements.txt

---

## 📌 Results

The Random Forest Regression model successfully predicts student exam scores using academic and behavioral factors. Hyperparameter tuning improved model performance, while AI-generated recommendations provide personalized guidance to help students improve their study habits and exam preparation.

---

## 👨‍💻 Author

**Abel Shibu**

Aspiring Data Analyst | Machine Learning Enthusiast | Cybersecurity Learner
import numpy as np #for numerical operation
import pandas as pd #for datasets
import seaborn as sns
import matplotlib.pyplot as plt #for visualization

data= pd.read_csv("/content/StudentPerformanceFactors.csv")#to load data set
data.head()#for display 1st 5 row

data.head()

data.dtypes

data.isna().sum()

data.shape

data['Teacher_Quality']=data['Teacher_Quality'].fillna(data['Teacher_Quality'].mode()[0])

data.isna().sum()

data['Parental_Education_Level']=data['Parental_Education_Level'].fillna(data['Parental_Education_Level'].mode()[0])

data['Distance_from_Home']=data['Distance_from_Home'].fillna(data['Distance_from_Home'].mode()[0])

data.isna().sum()

sns.boxplot(data)

plt.boxplot(data['Sleep_Hours'])
plt.title('box plot of ear sleep_hours')
plt.show()

plt.boxplot(data['Exam_Score'])
plt.title('box plot of ear sleep_hours')
plt.show()

data.head()

# encoding number_of_projects using label encoding
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

data['Parental_Involvement']=le.fit_transform(data['Parental_Involvement'])
data.head()

data['Access_to_Resources']=le.fit_transform(data['Access_to_Resources'])
data.head()

data['Extracurricular_Activities']=data['Extracurricular_Activities'].map({'No':0,'Yes':1})
data.head()

data['Motivation_Level'].nunique()

data['Motivation_Level']=le.fit_transform(data['Motivation_Level'])
data.head()

data['Internet_Access']=data['Internet_Access'].map({'No':0,'Yes':1})
data.head()

data['Family_Income']=le.fit_transform(data['Family_Income'])
data.head()

data['Teacher_Quality']=le.fit_transform(data['Teacher_Quality'])
data.head()

data['School_Type'].nunique()

data['School_Type']=le.fit_transform(data['School_Type'])
data.head()

data['Peer_Influence']=le.fit_transform(data['Peer_Influence'])
data.head()

data['Learning_Disabilities']=data['Learning_Disabilities'].map({'No':0,'Yes':1})
data.head()

data['Parental_Education_Level']=le.fit_transform(data['Parental_Education_Level'])
data.head()

data['Distance_from_Home']=le.fit_transform(data['Distance_from_Home'])
data.head()

data['Gender']=data['Gender'].map({'Female':0,'Male':1})
data.head()

features=[
    'Hours_Studied',
    'Attendance',
    'Previous_Scores',
    'Sleep_Hours'
]
target='Exam_Score'

X=data[features]
y=data[target]

sns.histplot(data['Exam_Score'])
plt.show()

corr=data[
    [
        'Hours_Studied',
        'Attendance',
        'Previous_Scores',
        'Sleep_Hours',
        'Exam_Score'
    ]
].corr()
corr

sns.heatmap(
    corr,
    annot=True,
    cmap='Blues'
)
plt.show()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor(random_state=42)
rf.fit(X_train,y_train)

pred=rf.predict(X_test)

from sklearn.metrics import r2_score #r2score should near 1
r2_score(y_test,pred)

from sklearn.model_selection import cross_val_score
score=cross_val_score(rf,X,y,cv=5)
score

from sklearn.model_selection import GridSearchCV ##hyper parameter tuning function for increase the r2 score for better result and we can use other methods to improve the r2 score

param_grid={
    'n_estimators':[100,200,300],
    'max_depth':[3,5,10,None],
    'min_samples_split':[2,5,10]
}

grid=GridSearchCV(RandomForestRegressor(random_state=42),param_grid,cv=5,scoring='r2')

grid.fit(X_train,y_train)

grid.best_params_

best_model=grid.best_estimator_

pred=best_model.predict(X_test)

r2_score(y_test,pred)

import joblib
joblib.dump(
    best_model,
    "student_model.pkl"
)

hours=5
attendence=75
previous=65
sleep=6

sample=pd.DataFrame(

        {
            'Hours_Studied':[hours],
            'Attendance':[attendence],
            'Previous_Scores':[previous],
            'Sleep_Hours':[sleep]
        }

)

predicted_score=best_model.predict(sample)[0]
predicted_score

prompt=f"""
you are an expert academic mentor
Student Details:
Hours Studied:{hours}
Attendence:{attendence}
previous_score:{previous}
Sleep Hours:{sleep}
Predicted Exam Score:{predicted_score:.2f}
Provide:
1. Study Improvement Plan
2. Daily Study Schedule
3. Revision Strategy
4. Time Management Tips
5. Exam Preparation
Use bullet points
"""

from google.colab import userdata
# Gemini API Key
# Replace with your own key when running
GOOGLE_API_KEY = "YOUR_API_KEY"

!pip install -q -U google-generativeai

import google.generativeai as genai
genai.configure(api_key=GOOGLE_API_KEY)

model=genai.GenerativeModel(
    'gemini-2.5-flash'
)

#1st prompt
response=model.generate_content(prompt)
print(response.text)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import pandas as pd
# import joblib
# import google.generativeai as genai
# 
# model=joblib.load("student_model.pkl")
# genai.configure(api_key=GOOGLE_API_KEY)
# gemini=genai.GenerativeModel(
#     'gemini-2.5-flash'
# )
# 
# st.title("Student Performance Predictor")
# hours=st.slider(
#     "Hours Studied",
#     0,
#     12,
#     5)
# attendence=st.slider(
#     "Attendence%",
#     0,
#     100,
#     75)
# previous=st.slider(
#     "Previous Score",
#     0,
#     100,
#     65)
# sleep=st.slider(
#     "Sleep Hours",
#     3,
#     10,
#     7)
# 
# if st.button("Predict Exam Score"):
#     sample=pd.DataFrame(
#         {
#             'Hours_Studied':[hours],
#             'Attendance':[attendence],
#             'Previous_Scores':[previous],
#             'Sleep_Hours':[sleep]
#         }
#     )
#     score=model.predict(sample)[0]
#     st.success(f"Predicted Exam Score:{score:.2f}")
#     prompt=f"""
# YouYou are an expert academic mentor
# Student Details:
# Hours Studied:{hours}
# Attendence:{attendence}
# previous_score:{previous}
# Sleep Hours:{sleep}
# Predicted Exam Score:{score:.2f}
# Provide:
# 1. Study Improvement Plan
# 2. Daily Study Schedule
# 3. Revision Strategy
# 4. Time Management Tips
# 5. Exam Preparation
# Use bullet points
# """
#     response=gemini.generate_content(prompt)
#     st.subheader(
#         "AI study coach"
#     )
#     st.write(response.text)

!pip install -q pyngrok

from pyngrok import ngrok
# ngrok token
NGROK_AUTH_TOKEN = "YOUR_NGROK_TOKEN"
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

!pip install streamlit

public_url=ngrok.connect(8501)
print(public_url)

!streamlit run app.py &>/content/logs.txt &

!npx localtunnel --port 8501


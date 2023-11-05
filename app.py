import pandas as pd 
import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import joblib
model =joblib.load('km_4_model.pkl')

lis = ["Age",	"Work_Experience",	"Family_Size",	"Gender_en",	"Ever_Married_en",	"Graduated_en",	"Profession_en","Spending_Score_en"]

st.title("Customer Segmentation")

Age = st.number_input("Age", 10, 100)
Work_Experience = st.number_input("Work Experiance", 0, 14)
Family_Size = st.number_input("Family Size", 0, 9)
# Gender_en = st.number_input(" Gender", 0, 1)
Gender_en = st.radio('Gender',['female','male'])
if Gender_en == 'female':
    Gender_en = 0
else:
    Gender_en = 1

Ever_Married_en = st.radio('Married Status',['Married','Unmarried'])
if Ever_Married_en == 'female':
    Ever_Married_en = 0
else:
    Ever_Married_en = 1
    

Graduated_en = st.radio(' Graduated Status',['Yes','No'])
if Graduated_en == 'female':
    Graduated_en = 0
else:
    Graduated_en = 1
Profession_en = st.number_input("Professionality", 0, 8)
Spending_Score_en = st.number_input("Spending ", 0, 2)

lis = [[Age,	Work_Experience,	Family_Size,	Gender_en,	Ever_Married_en,	Graduated_en,	Profession_en,	Spending_Score_en]]

if st.button("submit"):
    st.success(f"Segment no {model.predict(lis)[0]}")

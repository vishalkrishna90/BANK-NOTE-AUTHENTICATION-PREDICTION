from re import sub
import pandas as pd
import numpy as np
import streamlit as st
import warnings as war
war.filterwarnings('ignore')
import pickle as pkl

scaler = pkl.load(open('bna_scaler.pkl','rb'))
model = pkl.load(open('bna_model.pkl','rb'))

df = pd.read_csv('https://raw.githubusercontent.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/main/Clean_BankNote_Authentication.csv')


st.title('BANK NOTE AUTHENTICATION')

st.image('Images\\bank_note.jpg')

var,sek = st.columns(2)
with var:
    variance = st.slider('Enter Variance:',-7.0,6.0)	
with sek:
    skewness = st.slider('Enter Skewness:',-10.0,12.0)

cur,ent = st.columns(2)
with cur:
    curtosis = st.slider('Enter Curtosis:',-5.0,10.0)
with ent:
    entropy = st.slider('Enter Entropy:',-6.0,3.0)

submit = st.button('SUBMIT')

if submit:
    data = np.array([[variance,skewness,curtosis,entropy]])
    scale_data = scaler.transform(data)
    result = model.predict(scale_data)

    if result == 0:
        st.subheader('Note Is Original')
    else:
        st.subheader('Note Is Duplicate')
import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False)
model = pickle.load(open('model.pkl', 'wb'))


def main():
  st.sidebar.header("Do You Have Anxiety?")
  st.sidebar.header("Just fill in the information below")
  st.sidebar.header("XGBoost is used in this program")

  Sex =  st.slider("Input your gender 0=Female and 1=Male", 0,1)
  Age = st.slider("Input your age", 17,25)
  Year = st.slider("Your current year of study", 1,7)
  GPA = st.slider("What is your GPA?", 0.0,5.0)
  Status = st.slider("Input your marital status, 0=Single and 1=Married", 0,1)
  Depression = st.slider("Do you have depression? 0=No and 1=Yes", 0,1)
  Anxiety = st.slider("Do you have anxiety? 0=No and 1=Yes", 0,1)
  PanicAttack = st.slider("Do you have panick attack? 0=No and 1=Yes", 0,1)
  Treatment = st.slider("Did you seek any specialist for treatment? 0=No and 1=Yes", 0,1)
  inputs = [[Sex, Age, Year, GPA, Status, Depression, Anxiety, PanickAttack, Treatment]]

if st.button('Predict'):
  result = model.predict(inputs)
  updated_res = result.flatten().astype(int)
  if updated_res == 0:
    st.write("YESYESYES")
  elif updated_res == 1:
    st.write("NONONO")

if __name__ =='__main__':
  main()

  
  

import streamlit as st
import random
@st.cache_data
def generate_random_value(x): 
  return random.uniform(0, x) 
a = generate_random_value(10) 
b = generate_random_value(20) 
st.write(a) 
st.write(b)

joblib.load("model")
loaded_model = pickle.load(open("model", 'rb'))

import joblib
joblib.dump(clf, "model")

import pickle
pickle.dump(clf, open("model", 'wb'))

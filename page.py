import streamlit as st
import pandas as pd
import numpy as np
st.title("Hello Smriti")

data = pd.read_csv("Data//features_3_sec.csv")
print(data)
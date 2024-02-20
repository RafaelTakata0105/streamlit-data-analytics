import streamlit as st
import pandas as pd

st.title("Hola Mundo!")
st.header("Esto es un header")
st.markdown("*italic*")

file = "train.data"
df = pd.read_csv(file)
st.dataframe(df)


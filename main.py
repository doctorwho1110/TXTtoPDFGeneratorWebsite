import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import base64

dataset = st.file_uploader("upload file here", type=['csv'])
if dataset is not None:
    df = pd.read_csv(dataset)
    st.sidebar.write(' ### Rows and Columns:', df.shape)

    # Graph
    cols = list(df.columns)
    st.sidebar.write('### Columns:')
    check_boxes = [st.sidebar.checkbox(col, key=col) for col in cols]
    col1 = [col for col, checked in zip(cols, check_boxes) if checked]

    for i in col1:
        st.write('### ', i)
        st.line_chart(df[i])
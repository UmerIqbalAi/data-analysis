import streamlit as st# type: ignore
import pandas as pd# type: ignore
import matplotlib.pyplot as plt# type: ignore
import docx # type: ignore

# App Title and Styling
st.markdown("""
    <style>
    body {
        background-color: #1a1a1a;
        color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        color: #00ccff;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-title {
        font-size: 1.5rem;
        color: #ffffff;
        text-align: center;
        margin-bottom: 3rem;
    }
    .footer {
        font-size: 1rem;
        color: #00cff;
        text-align: center;
        margin-top: 5rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>Data Analysis App by Umer Iqbal</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-title'>Upload a CSV, Excel, or Word file for instant insights</h2>", unsafe_allow_html=True)

# File Uploader
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "docx"])

if uploaded_file is not None:
    file_name = uploaded_file.name
    st.markdown(f"### Analyzing: {file_name}")

    if file_name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        st.markdown("#### Basic Information")
        st.markdown(f"- Number of Rows: **{df.shape[0]}**")
        st.markdown(f"- Number of Columns: **{df.shape[1]}**")

        st.markdown("#### Column-wise Summary")
        st.write(df.describe())

        st.markdown("#### Data Visualization")
        st.bar_chart(df.select_dtypes(include='number'))

    elif file_name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
        st.dataframe(df)
        st.markdown("#### Basic Information")
        st.markdown(f"- Number of Rows: **{df.shape[0]}**")
        st.markdown(f"- Number of Columns: **{df.shape[1]}**")

        st.markdown("#### Column-wise Summary")
        st.write(df.describe())

        st.markdown("#### Data Visualization")
        st.line_chart(df.select_dtypes(include='number'))

    elif file_name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        full_text = " ".join([para.text for para in doc.paragraphs])
        word_count = len(full_text.split())
        st.markdown(f"#### Word Count: **{word_count}**")
        st.markdown("#### Document Preview")
        st.text_area("Content", full_text[:1000])

st.markdown("<div class='footer'>Crafted with ❤️ by Umer Iqbal</div>", unsafe_allow_html=True)

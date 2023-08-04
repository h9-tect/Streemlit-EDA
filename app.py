import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

# Define a function to load the data
@st.cache
def load_data(file):
    data = pd.read_csv(file)
    return data

# Define the Streamlit app
def main():
    st.title("Exploratory Data Analysis with Mito Spreadsheet and Streamlit")
    file = st.file_uploader("Upload a CSV file", type=["csv"])
    if file is not None:
        data = load_data(file)
        report = data.profile_report()
        st_profile_report(report)

if __name__ == "__main__":
    main()

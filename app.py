import streamlit as st
import pandas as pd
import pandas_profiling as pp
from mitosheet.streamlit.v1 import spreadsheet
from streamlit_pandas_profiling import st_profile_report

# Set page layout
st.set_page_config(layout="wide")

# Set page title
st.title('Tesla Stock Volume Analysis')

# Get CSV URL from user input
CSV_URL = st.text_input('Enter CSV URL')

# Load CSV data
try:
    data = pd.read_csv(CSV_URL)
except:
    st.warning('Invalid CSV URL. Please enter a valid CSV URL.')
    st.stop()

    # Perform EDA using pandas_profiling and Mito Spreadsheet
    report = pp.ProfileReport(data)
    new_dfs, code = spreadsheet(report.to_widgets())

    # Display EDA report
    st_profile_report(new_dfs)
    st.code(code)
else:
    st.warning('Please enter a CSV URL.')

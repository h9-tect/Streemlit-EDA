import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet
import pandas as pd
import plotly.express as px

# Set the page layout to wide
st.set_page_config(layout="wide")

# Set the title of the app
st.title('CSV Data Analysis with Mito Spreadsheet and Plotly')

# Allow the user to enter the CSV link
csv_url = st.text_input("Enter CSV URL", "")

# Load the CSV file if a valid URL is provided
if csv_url:
    try:
        df = pd.read_csv(csv_url)

        # Show raw data
        if st.checkbox('Show raw data'):
            st.write(df)

        # Data preprocessing (optional)
        # ...

        # Interactive filters (optional)
        # ...

        # Display the Mito spreadsheet for more interactive analysis
        st.subheader('Interactive Data Analysis')
        new_dfs, code = spreadsheet(df)

        # Data visualization using Plotly
        st.subheader('Data Visualization')
        fig = px.line(df, x='Date', y='Volume', title='Tesla Stock Volume over Time')
        st.plotly_chart(fig)

        # Display the code (optional)
        if st.checkbox('Show code'):
            st.code("""
import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet
import pandas as pd
import plotly.express as px

# Set the page layout to wide
st.set_page_config(layout="wide")

# Set the title of the app
st.title('CSV Data Analysis with Mito Spreadsheet and Plotly')

# Allow the user to enter the CSV link
csv_url = st.text_input("Enter CSV URL", "")

# Load the CSV file if a valid URL is provided
if csv_url:
    try:
        df = pd.read_csv(csv_url)

        # Show raw data
        if st.checkbox('Show raw data'):
            st.write(df)

        # Data preprocessing (optional)
        # ...

        # Interactive filters (optional)
        # ...

        # Display the Mito spreadsheet for more interactive analysis
        st.subheader('Interactive Data Analysis')
        new_dfs, code = spreadsheet(df)

        # Data visualization using Plotly
        st.subheader('Data Visualization')
        fig = px.line(df, x='Date', y='Volume', title='Tesla Stock Volume over Time')
        st.plotly_chart(fig)

        # Display the code (optional)
        if st.checkbox('Show code'):
            st.code(code)
    except Exception as e:
        st.error("Error: Invalid CSV URL or unable to load the data.")
        st.stop()
            """)
    except Exception as e:
        st.error("Error: Invalid CSV URL or unable to load the data.")

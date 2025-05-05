import streamlit as st
import pandas as pd
# Title of the app
st.title('CSV File Uploader and Filter')
# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# Check if a file is uploaded
if uploaded_file is not None:
    # Load the data using pandas
    df = pd.read_csv(uploaded_file)

    # Show the raw dataframe if checkbox is checked
    if st.checkbox('Show raw data'):
        st.write(df)

    # Show the dataframe in a table
    st.dataframe(df)
    # Selectbox to filter by a column (assuming there are at least 5 columns in the CSV)
    if len(df.columns) >= 5:
        column_to_filter = st.selectbox("Select column to filter by:", df.columns)

        # Show unique values from the selected column
        unique_values = df[column_to_filter].unique()
        selected_value = st.selectbox(f"Select a value from {column_to_filter}:", unique_values)

        # Filter the dataframe based on the selected value
        filtered_df = df[df[column_to_filter] == selected_value]

        # Show filtered data
        st.write(f"Showing data filtered by {column_to_filter} = {selected_value}")
        st.dataframe(filtered_df)
else:
    st.write("Please upload a CSV file to begin.")

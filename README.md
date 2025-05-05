code
![image](https://github.com/user-attachments/assets/9c99e891-0f06-42ee-9307-3eb7a434e6b5)

output
![Uploading image.png…]()

explanation
In this code, I created a Streamlit app that lets users upload a CSV file, view the data, and filter it based on a selected column. The app first asks the user to upload a CSV file using st.file_uploader(). Once the file is uploaded, I use the pandas library to load the data into a DataFrame, and the user can choose to view the raw data by checking a box.

The app also allows filtering the data by selecting a column and a value from that column using selectbox. If the CSV file has at least five columns, the user can pick one to filter by, and the app will display the filtered results. This makes it easy to explore and manipulate the data directly within the app, providing an interactive experience with CSV files.

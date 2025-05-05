code
![image](https://github.com/user-attachments/assets/18cab627-61e1-4249-899c-a20c05a6f7c7)
![image](https://github.com/user-attachments/assets/a8d01d95-223c-4c4b-a537-13b16a789aed)


output
![image](https://github.com/user-attachments/assets/5d42c6d0-5e02-424b-b0e4-99aaec9daa46)

explanation
In this Streamlit app, I connected to a MySQL database using SQLAlchemy to display and manipulate data from a "users" table. First, I created a connection to the database using the create_engine function and established a session using sessionmaker to interact with the database. The data from the "users" table is fetched using a SQL query and displayed as a table in the app using st.dataframe().

The app also includes two forms. The first form allows users to input their name and password to insert new rows into the "users" table. When the user submits the form, the app inserts the data into the database using a parameterized SQL query to prevent SQL injection attacks. The second form is for user authentication, where users can enter their username and password. The app verifies the credentials by querying the database with a parameterized query, and if the credentials are correct, a welcome message is shown. If the credentials are incorrect, an error message is displayed.

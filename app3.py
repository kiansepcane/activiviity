import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Set page title
st.set_page_config(page_title="NBA Stats Dashboard")

# Title of the app
st.title("NBA Basketball Stats Dashboard")

# Sidebar for User Input
st.sidebar.header("Filters")
players = ['LeBron James', 'Stephen Curry', 'Kevin Durant', 'Giannis Antetokounmpo', 'Luka Dončić']
selected_player = st.sidebar.selectbox("Select Player", players)

# Example API for NBA Player Stats (Replace with actual API)
# Here we use a mock dataset since we can't make API requests in this environment.
player_data = {
    "LeBron James": {
        "Points": 25.0, "Assists": 7.8, "Rebounds": 7.5, "Blocks": 1.1, "Steals": 1.3
    },
    "Stephen Curry": {
        "Points": 29.4, "Assists": 6.3, "Rebounds": 5.2, "Blocks": 0.4, "Steals": 1.3
    },
    "Kevin Durant": {
        "Points": 27.0, "Assists": 5.0, "Rebounds": 6.8, "Blocks": 1.1, "Steals": 0.7
    },
    "Giannis Antetokounmpo": {
        "Points": 28.1, "Assists": 5.9, "Rebounds": 11.0, "Blocks": 1.3, "Steals": 1.0
    },
    "Luka Dončić": {
        "Points": 27.5, "Assists": 8.6, "Rebounds": 8.0, "Blocks": 0.5, "Steals": 1.0
    }
}

# Fetch selected player's data
data = player_data[selected_player]

# Display basic player stats
st.subheader(f"Stats for {selected_player}")
st.write(f"Points per Game: {data['Points']}")
st.write(f"Assists per Game: {data['Assists']}")
st.write(f"Rebounds per Game: {data['Rebounds']}")
st.write(f"Blocks per Game: {data['Blocks']}")
st.write(f"Steals per Game: {data['Steals']}")

# Display player data as a DataFrame for charting
player_stats = {
    "Category": ["Points", "Assists", "Rebounds", "Blocks", "Steals"],
    "Stats": [data["Points"], data["Assists"], data["Rebounds"], data["Blocks"], data["Steals"]]
}
df = pd.DataFrame(player_stats)

# 1. Bar Chart (Matplotlib)
st.subheader(f"1. {selected_player} Stats Bar Chart")
fig, ax = plt.subplots()
ax.bar(df['Category'], df['Stats'], color=['blue', 'red', 'green', 'orange', 'purple'])
ax.set_ylabel('Stats')
ax.set_title(f'{selected_player} Stats by Category')
st.pyplot(fig)

# 2. Pie Chart (Plotly)
st.subheader(f"2. {selected_player} Stats Pie Chart")
fig_pie = px.pie(df, values='Stats', names='Category', title=f'{selected_player} Stats Distribution')
st.plotly_chart(fig_pie)

# 3. Line Chart (Matplotlib)
st.subheader(f"3. {selected_player} Stats Line Chart")
fig_line, ax = plt.subplots()
ax.plot(df['Category'], df['Stats'], marker='o', color='purple')
ax.set_ylabel('Stats')
ax.set_title(f'{selected_player} Stats by Category (Line Chart)')
st.pyplot(fig_line)

# 4. Scatter Plot (Plotly)
st.subheader(f"4. {selected_player} Stats Scatter Plot")
fig_scatter = px.scatter(df, x="Category", y="Stats", color="Category", title=f"{selected_player} Stats Scatter Plot")
st.plotly_chart(fig_scatter)

# 5. Area Chart (Plotly)
st.subheader(f"5. {selected_player} Stats Area Chart")
fig_area = px.area(df, x="Category", y="Stats", title=f"{selected_player} Stats Area Chart")
st.plotly_chart(fig_area)

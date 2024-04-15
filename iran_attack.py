import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("Iran's Attack on Israel 14/04/2024")

# Create DataFrame
final_df = pd.read_parquet('mapping_data.parquet')

# Convert latitude and longitude to float
final_df['Latitude'] = final_df['Latitude'].astype(float)
final_df['Longitude'] = final_df['Longitude'].astype(float)

# Function to plot data by time
def plot_data_by_time(selected_time):
    # Create a map centered at Israel
    m = folium.Map(location=[31.5, 34.75], zoom_start=8)
    for i, row in final_df[final_df['Time'] == selected_time].iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=row['numerical'],
            popup=f"{row['Location Name']} - {row['numerical']}",
            color='red',
            fill=True,
            fill_color='red'
        ).add_to(m)
    # Display the map
    # st.write(m._repr_html_(), unsafe_allow_html=True)
    # Display the map
    st_folium(m)

# Slider to select time
selected_time = st.select_slider('Select Time', options=sorted(final_df['Time'].unique()))

# Call the function to plot data by time
plot_data_by_time(selected_time)

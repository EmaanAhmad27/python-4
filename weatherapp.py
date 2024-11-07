import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

# Define the URLs for each city's weather page on BBC
city_urls = {
    "New York": "https://www.bbc.com/weather/5128581",
    "Faisalabad": "https://www.bbc.com/weather/1179400",
    "Islamabad": "https://www.bbc.com/weather/1176615",
    "Karachi": "https://www.bbc.com/weather/1174872",
    "Lahore": "https://www.bbc.com/weather/1172451",
    "Peshawar": "https://www.bbc.com/weather/1168197",
    "Quetta": "https://www.bbc.com/weather/1167528",
    "Multan": "https://www.bbc.com/weather/1169825",
    "Hyderabad": "https://www.bbc.com/weather/1176734",
    "Sialkot": "https://www.bbc.com/weather/1164909",
    "Rawalpindi": "https://www.bbc.com/weather/1166993",
    "Bahawalpur": "https://www.bbc.com/weather/1183880",
    "Sargodha": "https://www.bbc.com/weather/1166000",
    "Jhelum": "https://www.bbc.com/weather/1175864",
    "Chitral": "https://www.bbc.com/weather/1181065",
    "Gilgit": "https://www.bbc.com/weather/1178338",
    "Sibi": "https://www.bbc.com/weather/1164896",
    "Kalat": "https://www.bbc.com/weather/1175296",
    "Jacobabad": "https://www.bbc.com/weather/1176515",
    "Badin": "https://www.bbc.com/weather/1184055",
    "Zhob": "https://www.bbc.com/weather/1162105",
    "Jiwani": "https://www.bbc.com/weather/1175712",
    "Chor": "https://www.bbc.com/weather/1181022",
    "Paris": "https://www.bbc.com/weather/2988507",
    "Toronto": "https://www.bbc.com/weather/6167865",
    "Tokyo": "https://www.bbc.com/weather/1850147",
    "Chicago": "https://www.bbc.com/weather/4887398",
    "Lancaster": "https://www.bbc.com/weather/5197079",
    "Dammam": "https://www.bbc.com/weather/110336",
    "Istanbul": "https://www.bbc.com/weather/745044",
}

# List to store data for all cities
all_city_data = []

# Loop through each city and fetch weather data
for city, url in city_urls.items():
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract city name
        city_name = city

        # Extract temperature in Celsius
        temp_tag = soup.find('span', class_='wr-value--temperature--c')
        temperature = temp_tag.text.strip() if temp_tag else "Temperature not found"

        # Extract weather condition
        condition_tag = soup.find('div', class_='wr-day__weather-type-description')
        condition = condition_tag.text.strip() if condition_tag else "Condition not found"
        
        # Add icons based on condition using if-else statements
        if "Sunny" in condition:
            condition_with_icon = "☀️ " + condition
        elif "Partly cloudy" in condition:
            condition_with_icon = "⛅ " + condition
        elif "Cloudy" in condition or "Overcast" in condition:
            condition_with_icon = "☁️ " + condition
        elif "Rain" in condition:
            condition_with_icon = "🌧️ " + condition
        elif "Light rain" in condition:
            condition_with_icon = "🌦️ " + condition
        elif "Heavy rain" in condition:
            condition_with_icon = "🌧️ " + condition
        elif "Thunderstorm" in condition:
            condition_with_icon = "⛈️ " + condition
        elif "Snow" in condition:
            condition_with_icon = "❄️ " + condition
        elif "Fog" in condition or "Mist" in condition:
            condition_with_icon = "🌫️ " + condition
        elif "clear sky" in condition:
            condition_with_icon = "🌙" + condition
        elif "cloud" in condition:
            condition_with_icon = "☁️" + condition
        elif "wind" in condition or "windy" in condition:
            condition_with_icon = "💨" + condition
        elif "breeze" in condition:
            condition_with_icon = "🌬️" + condition
        else:
            condition_with_icon = condition  # No icon if condition doesn't match

        # Append data to the list
        all_city_data.append({
            "City": city_name,
            "Temperature (°C)": temperature,
            "Weather Condition": condition_with_icon
        })
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {city}: {e}")
        all_city_data.append({
            "City": city,
            "Temperature (°C)": "N/A",
            "Weather Condition": "N/A"
        })

# Create a DataFrame to display all data
df = pd.DataFrame(all_city_data)

# Convert "Temperature (°C)" to numeric values, handling non-numeric gracefully
df["Temperature (°C)"] = pd.to_numeric(df["Temperature (°C)"].str.extract(r'(-?\d+)')[0], errors='coerce')

# Sort the DataFrame by temperature in descending order (from hottest to coolest)
df = df.sort_values(by="Temperature (°C)", ascending=False, na_position='last')

# Reset the index to fix the numbering
df = df.reset_index(drop=True)

# Add a numbering column starting from 1
df['No.'] = range(1, len(df) + 1)

# Reorganize columns to display 'No.' first
df = df[['No.', 'City', 'Temperature (°C)', 'Weather Condition']]

# Streamlit display setup
st.title("🌍Current Weather in Major Cities of Pakistan")

st.markdown("<h4 style='font-weight:bold; font-size:20px;'>Search for a City</h4>", unsafe_allow_html=True)
search_city = st.text_input("")  # Empty label for input

# Filter the DataFrame based on user input
if search_city:
    filtered_df = df[df["City"].str.contains(search_city, case=False, na=False)]
else:
    filtered_df = df

# Convert the filtered DataFrame to HTML with custom header styling
html_rows = ""
for index, row in filtered_df.iterrows():
    city_cell = f"<td style='background-color: yellow'>{row['City']}</td>" if search_city and search_city.lower() in row["City"].lower() else f"<td>{row['City']}</td>"
    temp_cell = f"<td>{row['Temperature (°C)']}</td>"
    condition_cell = f"<td>{row['Weather Condition']}</td>"
    html_rows += f"<tr><td>{row['No.']}</td>{city_cell}{temp_cell}{condition_cell}</tr>"

# Add the HTML table structure with inline CSS for the header
html_table = f"""
<style>
    table {{
        width: 100%;
        border-collapse: collapse;
    }}
    th {{
        background-color: skyblue;
        font-weight: bold;
        padding: 10px;
        text-align: left;
    }}
    td {{
        padding: 10px;
    }}
</style>
<table border="1">
    <thead>
        <tr>
            <th>No.</th>
            <th>City</th>
            <th>Temperature (°C)</th>
            <th>Weather Condition</th>
        </tr>
    </thead>
    <tbody>
        {html_rows}
    </tbody>
</table>
"""

# Display the styled HTML table with highlighted search results in Streamlit
st.markdown(html_table, unsafe_allow_html=True)

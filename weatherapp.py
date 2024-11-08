import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

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

all_city_data = []

for city, url in city_urls.items():
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        city_name = city
        temp_tag = soup.find('span', class_='wr-value--temperature--c')
        temperature = temp_tag.text.strip() if temp_tag else "Temperature not found"
        condition_tag = soup.find('div', class_='wr-day__weather-type-description')
        condition = condition_tag.text.strip() if condition_tag else "Condition not found"
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
            condition_with_icon = "🌬️ " + condition
        else:
            condition_with_icon = condition  
        
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
df = pd.DataFrame(all_city_data)
df["Temperature (°C)"] = pd.to_numeric(df["Temperature (°C)"].str.extract(r'(-?\d+)')[0], errors='coerce')
st.title("🌍Current Weather in Some Cities of the World")
st.markdown("<h4 style='font-weight:bold; font-size:20px;'>Search for a City</h4>", unsafe_allow_html=True)
search_city = st.text_input("")
st.markdown("<h4 style='font-weight:bold; font-size:20px;'>Sort by</h4>", unsafe_allow_html=True)
sort_option = st.selectbox("", ["Temperature: High to Low", "Temperature: Low to High", "City: A to Z", "City: Z to A"])
if search_city:
    filtered_df = df[df["City"].str.contains(search_city, case=False, na=False)]
else:
    filtered_df = df
if sort_option == "Temperature: High to Low":
    filtered_df = filtered_df.sort_values(by="Temperature (°C)", ascending=False, na_position='last')
elif sort_option == "Temperature: Low to High":
    filtered_df = filtered_df.sort_values(by="Temperature (°C)", ascending=True, na_position='last')
elif sort_option == "City: A to Z":
    filtered_df = filtered_df.sort_values(by="City", ascending=True)
elif sort_option == "City: Z to A":
    filtered_df = filtered_df.sort_values(by="City", ascending=False)
filtered_df = filtered_df.reset_index(drop=True)
filtered_df['No.'] = range(1, len(filtered_df) + 1)
filtered_df = filtered_df[['No.', 'City', 'Temperature (°C)', 'Weather Condition']]
html_rows = ""
for index, row in filtered_df.iterrows():
    city_cell = f"<td style='background-color: yellow'>{row['City']}</td>" if search_city and search_city.lower() in row["City"].lower() else f"<td>{row['City']}</td>"
    temp_cell = f"<td>{row['Temperature (°C)']}</td>"
    condition_cell = f"<td>{row['Weather Condition']}</td>"
    html_rows += f"<tr><td>{row['No.']}</td>{city_cell}{temp_cell}{condition_cell}</tr>"

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
st.markdown(html_table, unsafe_allow_html=True)

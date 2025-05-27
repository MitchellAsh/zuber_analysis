# main.py

# =========================================================================
# Imports
# =========================================================================
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# =========================================================================
# Get Weather Data
# =========================================================================
def get_weather_data():
    """Fetch weather data by scraping the HTML table with id 'weather_records' and return as DataFrame."""
    url = "https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find('table', attrs={"id": "weather_records"})

    # Extract headers
    heading_table = [th.text for th in table.find_all('th')]

    # Extract rows
    content = []
    for row in table.find_all('tr'):
        if not row.find_all('th'):  # skip header rows
            content.append([td.text for td in row.find_all('td')])

    # Create DataFrame
    weather_records = pd.DataFrame(content, columns=heading_table)

    # Convert Temperature to float to prevent issues later on
    weather_records['Temperature'] = weather_records['Temperature'].astype(float)

    return weather_records

# =========================================================================
# Clean Weather Data
# =========================================================================
def clean_weather_data(weather_df):
    """Format weather datetime and convert temperature from Kelvin to Celsius."""
    weather_df['Date and time'] = pd.to_datetime(weather_df['Date and time'], format='%Y-%m-%d %H:%M:%S')
    weather_df['Temperature_C'] = weather_df['Temperature'] - 273.15
    weather_df['hour'] = weather_df['Date and time'].dt.floor('H')
    return weather_df

# =========================================================================
# Load Trip Data
# =========================================================================
def load_trip_data():
    """Load trip data from a CSV file and return it as a DataFrame."""
    trip_df = pd.read_csv('data/trips.csv')
    print(trip_df.head())
    return trip_df

# =========================================================================
# Clean Trip Data
# =========================================================================
def clean_trip_data(trip_df):
    """Convert start timestamps to datetime and floor to hour."""
    trip_df['start_ts'] = pd.to_datetime(trip_df['start_ts'], unit='s')
    trip_df['hour'] = trip_df['start_ts'].dt.floor('H')
    return trip_df

# =========================================================================
# Merge DataFrames
# =========================================================================
def merge_data(weather_df, trip_df):
    """Merge weather and trip data on the 'hour' column."""
    merged_df = pd.merge(trip_df, weather_df, on='hour', how='left')
    print(f"Merged DataFrame shape: {merged_df.shape}")
    return merged_df

# =========================================================================
# Analyze Merged Data
# =========================================================================
def analyze_data(merged_df):
    """Perform analysis to investigate effect of weather on trip duration."""
    avg_duration_by_weather = merged_df.groupby('Description')['duration_seconds'].mean().sort_values()
    print("\nAverage trip duration by weather condition:\n")
    print(avg_duration_by_weather)

# =========================================================================
# Main Function
# =========================================================================
def main():
    """Main function to execute the data processing pipeline."""
    weather_df = get_weather_data()
    weather_df = clean_weather_data(weather_df)

    trip_df = load_trip_data()
    trip_df = clean_trip_data(trip_df)

    merged_df = merge_data(weather_df, trip_df)

    # Save the merged DataFrame to a CSV file for analysis in a notebook
    merged_df.to_csv("data/merged_data.csv", index=False)
    print("Merged data exported to data/merged_data.csv")

    analyze_data(merged_df)

# =========================================================================
# Script Entry Point
# =========================================================================
if __name__ == "__main__":
    main()

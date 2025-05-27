# Import necessary libraries
import pandas as pd
import requests

# Function to fetch and process weather data
def get_weather_data():
    # Fetch the HTML content from the URL
    url = "https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html"
   
    # Make a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    response.raise_for_status() 

    # Parse the HTML content and extract tables
    tables = pd.read_html(response.text)

    # Check if any tables were found
    print(f"Number of tables found: {len(tables)}")

    # If tables were found, return the first one
    weather_df = tables[0]
    
    # Display the first few rows of the DataFrame
    print(weather_df.head())
    
    # Return the DataFrame
    return weather_df

# Run the function if this script is executed directly
if __name__ == "__main__":
    # Call the function to get weather data
    weather_data = get_weather_data()
# zuber_analysis
Zuber Ride-Sharing Analysis Project - Summary

Goal:
Analyze taxi data in Chicago to understand passenger preferences and the impact of weather on ride frequency.

Data:
- neighborhoods: neighborhood_id, name
- cabs: cab_id, vehicle_id, company_name
- trips: trip_id, cab_id, start_ts, end_ts, duration_seconds, distance_miles, pickup_location_id, dropoff_location_id
- weather_records: record_id, ts, temperature, description

Steps:
1. Parse November 2017 weather data from HTML.
2. SQL Data Analysis:
   - Count rides per company on Nov 15–16.
   - Count rides for "Yellow" or "Blue" companies (Nov 1–7).
   - Analyze Flash Cab, Taxi Affiliation Services, and others.
3. Hypothesis Testing Preparation:
   - Identify Loop (id 50) and O'Hare (id 63).
   - Categorize weather as "Good"/"Bad".
   - Retrieve rides from Loop to O'Hare on Saturdays with weather and duration data.
4. Python EDA:
   - Use project_sql_result_01.csv (rides per company).
   - Use project_sql_result_04.csv (avg drop-offs per neighborhood).
   - Visualize and interpret data.
5. Hypothesis Testing in Python:
   - Use project_sql_result_07.csv (Loop to O'Hare rides with weather and durations).
   - Test: "Avg duration changes on rainy Saturdays."
   - Set alpha, define null/alt hypotheses, explain statistical test and conclusion.

Evaluation Criteria:
- Data parsing, slicing, grouping, joining.
- Hypothesis formation and testing.
- Commenting and conclusions.

URL for weather HTML data:
https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html


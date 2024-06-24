Analyzing Disaster Impact on Nearby Cities Using Geographic Data and API Integration

I developed a program that analyzes disaster data in relation to a user-specified city. Here’s a quick breakdown of how it works:

1) Load Data: The program reads disaster and city data from CSV files.
2) Get Coordinates: It retrieves the geographical coordinates of the user-specified city using the Google Maps API.
3) Nearby Cities: It calculates a radius around the city and finds nearby cities within that radius.
4) Country Code: The program determines the country code of the user-specified city.
5) Disaster Data Filtering: It filters disaster data for the nearby cities and matches it with the country's ISO code.
6) Create JSON File: Finally, it compiles the relevant data and saves it as a JSON file.

Key Features
1) Uses Google Maps API to get city coordinates and country codes.
2) Finds nearby cities within a specified radius.
3) Filters and extracts relevant disaster data.
4) Outputs the results in a structured JSON file.

This program is useful for analyzing how disasters impact cities within a certain proximity of a specified location.


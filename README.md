# Rick and Morty API Character Analysis

### Introduction

The Rick and Morty API Character Analysis project is designed to fetch character data from the Rick and Morty API, process the data, and store it in a Google BigQuery table for further analysis. 
The project utilizes Python libraries such as requests, pandas_gbq, and pandas to interact with the API, handle data, and perform data loading into Google BigQuery.

### Project Overview

The main components of the project include:

1- API Interaction: The project interacts with the Rick and Morty API to fetch character data using HTTP requests.

2- Data Processing: The fetched data is processed to extract relevant information such as character names, locations, and episode counts.

3- Data Analysis: The processed data is structured into a DataFrame using the pandas library, allowing for data manipulation and analysis.

4- Data Loading: The final DataFrame is loaded into a Google BigQuery table using the pandas_gbq library, enabling storage and analysis in a scalable cloud-based data warehouse.

### Customizing the code

Update the project with your Google Cloud project ID and BigQuery table ID in the script where indicated:
```
pandas_gbq.to_gbq(chars_df, 'table_id', project_id='project_id', if_exists='append')
```

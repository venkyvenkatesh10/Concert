import pandas as pd

# Load the generated concert data
concert_data_file = 'C:/Users/venka/Downloads/Concert10/Generated Data/generated_concert_data.csv'
concert_data = pd.read_csv(concert_data_file)

# Load the generated app usage data
app_usage_data_file = 'C:/Users/venka/Downloads/Concert10/Generated Data/generated_app_usage_data.csv'
app_usage_data = pd.read_csv(app_usage_data_file)

# Load the generated location CMA data
location_cma_data_file = 'C:/Users/venka/Downloads/Concert10/Generated Data/generated_location_cma_data.csv'
location_cma_data = pd.read_csv(location_cma_data_file)

# Select the columns to join from app usage data
app_usage_columns = ["Upstream Data (MB)", "Downstream Data (MB)", "App Name", "Timestamp"]

# Select the columns to join from location CMA data
location_cma_columns = ["City", "State", "Country", "Zip code"]

# Concatenate the dataframes
joined_data = pd.concat([concert_data, app_usage_data[app_usage_columns], location_cma_data[location_cma_columns]], axis=1)

# Save the result to a new CSV file
output_file = 'C:/Users/venka/Downloads/Concert10/Generated Data/joined_concert_app_location_data.csv'
joined_data.to_csv(output_file, index=False)

print("Joined CSV file has been created successfully.")

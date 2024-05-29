import csv
import random
from datetime import datetime, timedelta
import faker

# Initialize faker for generating random data
fake = faker.Faker()

# Define the number of rows to generate
num_rows = 10000

# Define the headers
headers = ["First Name", "Last Name", "Upstream Data (MB)", "Downstream Data (MB)", "App Name", "Timestamp"]

# Define possible app names
app_names = ["Facebook", "Instagram", "Twitter", "Snapchat", "YouTube", "WhatsApp", "TikTok"]

# Generate data and write to CSV file
with open('generated_app_usage_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    
    for _ in range(num_rows):
        first_name = fake.first_name()
        last_name = fake.last_name()
        upstream_data = round(random.uniform(0.1, 100.0), 2)  # Upstream data between 0.1 MB and 100.0 MB
        downstream_data = round(random.uniform(0.1, 500.0), 2)  # Downstream data between 0.1 MB and 500.0 MB
        app_name = random.choice(app_names)
        timestamp = fake.date_time_between(start_date='-1y', end_date='now').strftime("%Y-%m-%d %H:%M:%S")
        
        writer.writerow([first_name, last_name, upstream_data, downstream_data, app_name, timestamp])

print("CSV file has been created successfully.")

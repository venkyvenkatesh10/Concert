import csv
import random
import faker

# Initialize faker for generating random data
fake = faker.Faker()

# Define the number of rows to generate
num_rows = 10000

# Define the headers
headers = ["First Name", "Last Name", "Network Provider", "Total Data (GB)", "Age"]

# Define possible network providers
network_providers = ["Verizon", "AT&T", "T-Mobile", "Sprint"]

# Generate data and write to CSV file
with open('generated_concert_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    
    for _ in range(num_rows):
        first_name = fake.first_name()
        last_name = fake.last_name()
        network_provider = random.choice(network_providers)
        total_data_gb = round(random.uniform(0.5, 10.0), 6)
        age = random.randint(18, 100)
        
        writer.writerow([first_name, last_name, network_provider, total_data_gb, age])

print("CSV file has been created successfully.")

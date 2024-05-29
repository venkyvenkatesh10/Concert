import csv
import faker

# Initialize faker for generating random data
fake = faker.Faker()

# Define the number of rows to generate
num_rows = 10000

# Define the headers
headers = ["First Name", "Last Name", "City", "State", "Country", "Zip code"]

# Generate data and write to CSV file
with open('generated_location_cma_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    
    for _ in range(num_rows):
        first_name = fake.first_name()
        last_name = fake.last_name()
        city = fake.city()
        state = fake.state()
        country = fake.country()
        zip_code = fake.zipcode()
        
        writer.writerow([first_name, last_name, city, state, country, zip_code])

print("CSV file has been created successfully.")

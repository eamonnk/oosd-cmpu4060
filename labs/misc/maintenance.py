import random
import faker
import csv

# Initialize Faker instance
fake = faker.Faker()

# Function to generate random payment data
def generate_maintenance(num_rows):
    data = []
    for _ in range(num_rows):
        event_id = fake.unique.random_int(min=1, max=999999)
        #payment_type = random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Apple Pay', 'Google Pay'])
        # payment_provider = random.choice(['Visa', 'MasterCard', 'American Express', 'Discover', 'PayPal', 'Stripe'])
        credit_card_number = random.randint(1000000000000000, 9999999999999999)
        exp_date = f"{random.randint(1, 12):02d}/{random.randint(23, 30)}"  # Expiry date in MM/YY format
        data.append((payment_id, payment_type, payment_provider, credit_card_number, exp_date))
    return data

# Generate 50 rows of realistic payment data
payment_data = generate_payment_data(50)

# Define file path for CSV output
file_path = "payment_methods_data.txt"

# Write data to CSV
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['payment_ID', 'payment_type', 'payment_provider', 'credit_card_number', 'exp_date'])  # Column headers
    writer.writerows(payment_data)

print(f"CSV file with payment data has been saved to {file_path}")

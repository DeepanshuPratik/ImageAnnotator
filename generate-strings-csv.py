import csv
import random
import string

def generate_random_string(length=11):
    """Generate a random string of given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_csv_with_random_strings(filename, num_strings=5, string_length=10):
    with open(filename, 'r') as f:
        file_content = f.read()
    print(file_content)
    """Generate a CSV file containing random strings."""
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Random String'])
        for _ in range(num_strings):
            csv_writer.writerow([generate_random_string(string_length)])

if __name__ == "__main__":
    generate_csv_with_random_strings('random_strings.csv')
    print("CSV file generated successfully.")


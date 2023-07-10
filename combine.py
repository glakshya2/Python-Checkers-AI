import csv
import os

# Number of CSV files to combine
num_files = 15

# Existing combined CSV file
existing_file = "data.csv"

# Open the existing combined CSV file in read mode
with open(existing_file, 'r') as existing_csv:
    reader = csv.reader(existing_csv)
    existing_data = list(reader)

# Create a new combined CSV file
combined_file = "data.csv"

# Open the combined CSV file in write mode
with open(combined_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    # Write the existing data to the combined file
    writer.writerows(existing_data)

    # Loop through each CSV file
    for i in range(num_files):
        file_name = f"data{i}.csv"

        # Open the current CSV file
        with open(file_name, 'r') as infile:
            reader = csv.reader(infile)

            # Skip the header row if it's the first file
            if i > 0:
                next(reader)

            # Write each row from the current file to the combined file
            for row in reader:
                writer.writerow(row)

print(f"Combined contents of {num_files} CSV files into {combined_file}.")

# -*- coding: utf-8 -*-
import sys
import os
import csv

print(sys.argv)
# prints the parameters from the shell
# terminal : python myFile.py credit_card.csv
# for ex : ['myFile.py', 'fileName.csv']
os.mkdir('CCFolder') # making a directory

# now we are working on python to do the task
input_file = sys.argv[1]  # Replace with your actual file path
output_file = '/home/asmaalafe55/CCFolder/newFile.py'  # Replace with your desired output file path

try:
    total_amount = 0  # Initialize the total amount

    # Open the input file and read data
    with open(input_file, mode='r') as infile:
        csv_reader = csv.DictReader(infile)  # Read rows as dictionaries

        # Open the output file to write filtered rows
        with open(output_file, mode='w', newline='') as outfile:
            fieldnames = csv_reader.fieldnames  # Get column headers
            csv_writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            # Write the header to the new file
            csv_writer.writeheader()

            # Filter and process rows
            for row in csv_reader:
                if row['IsFraud'] == '1':  # Check if IsFraud is 1
                    csv_writer.writerow(row)  # Write to the new file
                    total_amount += float(row['Amount'])  # Add to total amount

    # Print the total amount
    print(f"The total amount of fraudulent transactions is: {total_amount}")

except Exception as e:
    print(f"An error occurred: {e}")



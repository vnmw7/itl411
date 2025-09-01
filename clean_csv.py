
import csv

with open('yes.csv', 'r') as infile, open('yes_cleaned.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)
    writer.writerow(header)
    for row in reader:
        if len(row) > 5:
            # Join the last parts of the row to form the date
            row[4] = ','.join(row[4:])
            # Keep only the first 5 elements
            row = row[:5]
        writer.writerow(row)

print("CSV file has been cleaned and saved as yes_cleaned.csv")

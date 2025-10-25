#reading csv file
import csv
with open('sample_data.csv','r') as file:
    csv_reader=csv.reader(file)
    print(csv_reader)
    for row in csv_reader:
#filtering customers in hyderabad location
        if row[3]=='hyderabad':
#filtering  only gmail users
            if row[1].endswith('gmail.com'):
                print(row)

#reading as dictionary in csv file
with open('sample_data.csv','r') as file:
    csv_reader=csv.DictReader(file)
    for rows in csv_reader:
        #print(rows)
        if rows['email'].endswith('@yahoo.com'):
            print(rows)
#appending in csv file
with open('sample_data.csv','a') as file:
    csv_reader=csv.writer(file)
    csv_reader.writerow(['vyshu','vyshu@gmail.com',797348,'hyderabad'])
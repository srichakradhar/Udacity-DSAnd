"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
telephone_numbers = set()
for log in texts:
    telephone_numbers.add(log[0])
    telephone_numbers.add(log[1])

for log in calls:
    telephone_numbers.add(log[0])
    telephone_numbers.add(log[1])
    

print("There are %d different telephone numbers in the records." % len(telephone_numbers))

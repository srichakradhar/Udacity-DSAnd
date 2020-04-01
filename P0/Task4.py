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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# receivers = set([log[1] for log in calls]).union(set([log[0] for log in texts])).union(set([log[1] for log in texts]))
# set([log[0] for log in calls]) - receivers

receivers = set()
for log in texts:
    receivers.add(log[0])
    receivers.add(log[1])


callers = set()
for log in calls:
    callers.add(log[0])
    receivers.add(log[1])


print("These numbers could be telemarketers: ")
for number in sorted(callers - receivers):
    print(number)

"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
duration = {}
duration_log = 0
longest = 0
for log in calls:
    duration_log = int(log[3])
    for number in log[0:2]:
        if number not in duration:
            duration[number] = duration_log
            if duration_log > longest:
                longest = duration_log
                batting_baba = number
        else:
            duration[number] += duration_log
            if duration[number] > longest:
                longest = duration[number]
                batting_baba = number


print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(batting_baba, longest))

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

text_senders = set()
text_receivers = set()
callers = set()
callees = set()
for x in texts:    # 32
    text_senders.add(x[0])
    text_receivers.add(x[1])

for x in calls:    # 36
    callers.add(x[0])
    callees.add(x[1])

possible_telemarketers = set()
for caller in callers:   #41
    if  not caller in text_senders and not caller in text_receivers and not caller in  callees:
            possible_telemarketers.add(caller)


print("These numbers could be telemarketers: ")
for number in sorted(possible_telemarketers): #47
    print(number)


"""
The Worst case time complexity is O(n log n), where n is size of texts
list and calls list combined. 

Explanation:
As sorting time will be more dominant for sufficiently large n, we can ignore
the O(n) - the time to add items in the sets callers, callees and
possible_telemarketers. 

The time complexity of python operations are based on https://wiki.python.org/moin/TimeComplexity
"""



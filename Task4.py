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
The Worst case time complexity is O(x + y log y), where x is size if texts
list, and y is the size of calls list.

Explanation:
On line #32, the time complexity is O(x) + O(x) -> O(2x) -> O(x), where x is
size of the texts list.
On line #36, by the same reasoning, the time complexity is O(y), where y is the
size of calls list.
On line #41, the worst case time complexity of adding an item to a set of (possible
size y is O(y) 
On line #47, the time complexity is equal to the the sorting time complexy of
list possible_telemarketers of max possible size y is O(y log y). The reasoning
being, in the worst case scenario, if all callers are telemarketers, the size
of possible_telemarketers list will be the same as the size of calls list.

Combining all time complexities done serially: O(x + y +  y log y)
Simplifying by dropping, the non-determinant term y: O(x + y log y)

The time complexity of python operations are based on https://wiki.python.org/moin/TimeComplexity
"""



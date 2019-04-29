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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

print("First record of texts, {0} texts {1} at time {2}".format(texts[0][0],texts[0][1],texts[0][2]))
print("Last record of call, {0} calls {1} at time {2}".format(calls[-1][0],calls[-1][1],calls[-1][2]))


"""
Big O analysis: O(1)

As per https://wiki.python.org/moin/TimeComplexity, "Get item" time complexity
There are 4 Python list lookup operations regardless of the input  size. 
is  O(1). 

Therefore, the worst case time will be: O(1)*4. The constant term 4 is non
deteminant factor in the time analysis and can be dropped.  
"""

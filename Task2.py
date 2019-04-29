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

totals = {}
for c in  calls:
    totals[c[0]] = totals[c[0]]+int(c[3]) if c[0] in totals else int(c[3])
    totals[c[1]]=  totals[c[1]]+int(c[3]) if c[1] in totals else int(c[3])

sorted_totals = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".
      format(sorted_totals[0][0],sorted_totals[0][1]))


"""
Big O Analysis: O(n log n)

According to https://wiki.python.org/moin/TimeComplexity, the worst case time complexity of
adding an item to a dictionary is O(n) where n is the size of the dictionary. 
Ignoring the non-dominiant constant term, we spend O(n) time population totals
dictionary. 

Sorting the dictionary takes O(n log n) time. Therefore, the full time
complexity is: O(n + n log n). Solving further. 
O(n(1+ log n))
O(n log n) # dropping the constant term)

In other words, sorting time is more dominant than time taken to add items in
the dictionary.
"""



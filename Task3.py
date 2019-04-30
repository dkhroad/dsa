"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import bisect
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


# part A
def is_bangalore_number(number):
    return True if number.startswith('(080)') else False

def extract_code(number):
    # print(number)
    match = re.search('^\((\d+)\)',number)
    if match:
        return match.group(1)
    return  number[:4]

called_area_codes = []
total_called = 0
total_local_calls = 0

for call in calls:                             #65
    if is_bangalore_number(call[0]):
        # print(call[0],call[1])
        total_called += 1
        area_code = extract_code(call[1])
        if area_code  == "080":
            total_local_calls += 1
        if not area_code in called_area_codes:
            called_area_codes.append(area_code) #73

print("The numbers called by people in Bangalore have codes:")
for area_code in sorted(called_area_codes): # 76
    print(area_code)

# part B
print("{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format((total_local_calls/total_called) * 100))


"""
Big O Analysis for part A: O(n log n), where n is the size of calls list. 

Explanation:
Time complexity to  compute numbers called from fixed lines in Bangalore: O(n).
The amount of work done in functions is_bangalore_number() and extract_code()
is rougly constant and is equal to O(1), 

The worst case time (amortized) complexity of adding a area_code to 
'called_area_codes' list on line 73 is O(x), where x is the size of area_code
list. In the worst case, x could be same as n (size of the calls list); if,
every number is called by Bangalore area code. 

The time complexity of line #76 is time to sort the called_area_codes list that
is assumed to be O(n log n). 

Therefore, the total worst case time complexity of part A is: 1) time to add
area coded to the called_area_codes list, 2) time to sort the called_area_codes
list. The total time complexity then is: O(n + n log n). That is asymptotically
equal to O(n log n).

for the part b, assuming the format call, multiplicaton and division takes a 
constant amout of time; the time complexity is O(1).
"""

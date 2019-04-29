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

def different_telephone_numbers(texts):
    """returns unique telephone numbers.
    assumption: this method assumes that a telephone number 
    doesn't exist in multiple formats. 
    """
    tel_numbers =  set()
    for t in texts:
        tel_numbers.update(t[0],t[1])

    return  len(tel_numbers)


print("There are {0} different telephone numbers in the records.".
      format(different_telephone_numbers(texts) + 
             different_telephone_numbers(calls)));

""" 
Big O: O(x+y) 

According to https://wiki.python.org/moin/TimeComplexity, the worst case 
(amortized) time complexity of set time is O(n), where n is the size of a set/dictonary. 
of a set lookup operation is same is dictionary lookup up operation. 
Here,we add 2x objects to texts set and 2y objects to calls set.
Therefore,ignoring the constant terms, worst cast time complexity will O(x+y) 
  
"""


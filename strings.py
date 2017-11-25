myString = 'Hello World!'
print(myString)        # Prints complete myStringing
print(myString[0])       # Prints first character of the myStringing
print(myString[2:5])     # Prints characters starting from 3rd to 5th
print(myString[2:])    # Prints myStringing starting from 3rd character
print(myString * 2)    # Prints myStringing two times
print(myString + "TEST")  # Prints concatenated myStringing
print("My name is %s and weight is %d kg!" % ('Zara', 21))  # string format
# list examples
myList = ['abcd', 786, 2.23, 'john', 70.2]
tinyList = [123, 'john']

print(myList)          # Prints complete list
print(myList[0])       # Prints first element of the list
print(myList[1:3])     # Prints elements starting from 2nd till 3rd
print(myList[2:])      # Prints elements starting from 3rd element
print(tinyList * 2)  # Prints list two times
print(myList + tinyList)  # Prints concatenated lists
# Tuples can be thought of as read-only lists
myTuple = ('abcd', 786, 2.23, 'john', 70.2 )
tinyTuple = (123, 'john')

# dictionary
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])       # Prints value for 'one' key
print(dict[2])           # Prints value for 2 key
print(tinydict)          # Prints complete dictionary
print(tinydict.keys())   # Prints all the keys
print(tinydict.values())  # Prints all the values

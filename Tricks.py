# http://anandology.com/python-practice-book/iterators.html

def __mul__(selfy, other):
    if len(other) != len(selfy):
        raise ValueError("Number of dimensions of multiplied vectors must be equal.")
    return sum(a * b for a, b in zip(selfy, other))


myZip = zip(['a', 'b', 'c'], [1, 2, 3])
print(myZip)
for el in myZip:
    print(el)
myDot = __mul__([1, 2, 3], [4, 5, 1])
print(myDot)

a_gen = (x*x for x in range(10)) # generator object created
print(a_gen)
print(sum(a_gen))

def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

def squares():
    for i in integers():
        yield i * i


ser_sq = squares()
print(ser_sq.__next__())
print(ser_sq.__next__())
print(ser_sq.__next__())

myBreak = 4
for i in ser_sq:
    print(i)
    myBreak -= 1
    if myBreak <= 0:
        break

print("The end")

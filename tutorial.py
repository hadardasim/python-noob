import sys
# If you are running new version of Python, then you would need to use print statement with parenthesis
print("hello world")
if True:
    print("True")
    print("True2")  # this is the second line in the block
else:
    print("False")
# a new block start due to change in indent
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
print(paragraph)
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)
x = 'foo'; sys.stdout.write(x + '\n')
# raw_input("\n\nPress the enter key to exit.")  # we get an error for this line in windows and python 3.6

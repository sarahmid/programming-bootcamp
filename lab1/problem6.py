"""
What does raw_input() do? Google it and see if you're right.

https://docs.python.org/2/library/functions.html#raw_input

raw_input() allows you to get user input from the terminal. Execution pauses until the user enters some text and hits "enter" in the terminal. The input is then converted to a string and can be saved in a variable, as we did in the example.
"""

print "Enter your name"
firstName = raw_input("First name:")
lastName = raw_input("Last name:")
print "Welcome,", firstName, lastName

"""
Run this. What is different about the output?
Now there's a "prompt" on the same line instead of the line before. (This is not necessarily better, it's just another way of doing it.)
"""
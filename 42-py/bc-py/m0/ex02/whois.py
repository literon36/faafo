import sys

# if no argument is provided, print usage
if len(sys.argv) == 1:
    print("Usage: python whois.py <number>")
    sys.exit()

# if more than one argument is provided, print error
if len(sys.argv) > 2:
    print("Error: too many arguments")
    sys.exit()

# if the argument is not an integer, print an error message
if not sys.argv[1].isdigit():
    print("Error: argument is not a digit")
    sys.exit()

# check if the argument is 0, even or odd
if int(sys.argv[1]) == 0:
    print("I'm Zero.")
elif int(sys.argv[1]) % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")

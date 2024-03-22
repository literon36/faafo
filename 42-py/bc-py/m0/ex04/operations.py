import sys

# if no argument is provided, print usage
if len(sys.argv) == 1:
    print("Usage: python operations.py <number1> <number2>")
    print("Example: python operations.py 10 3")
    sys.exit()

# if more than two arguments are provided, print error
if not len(sys.argv) == 3:
    print("Error: invalid number of arguments")
    sys.exit()

# if the arguments are not numbers, print an error message
if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("Error: only numbers are allowed")
    sys.exit()

a :int = int(sys.argv[1])
b :int = int(sys.argv[2])

# sum a and b
sum :str = str(a + b)
print("Sum:         " + sum)

# difference between a and b
diff :str = str(a - b)
print("Difference:  " + diff)

# product of a and b
prod :int = a * b
print("Product:     " + str(prod))

# quotient of a and b
if b == 0:
    quot :str = "Error: division by zero"
else:
    quot :str = str(a / b)
print("Quotient:    " + quot)

# remainder of a and b
if b == 0:
    rem :str = "Error: division by zero"
else:
    rem :str = str(a % b)
print("Remainder:   " + rem)

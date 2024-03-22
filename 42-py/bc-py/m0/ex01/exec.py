import sys

# total arguments
n : int = len(sys.argv)

# if no arguments then return nothing
if n == 1:
    print("Pass at least one argument")
    sys.exit()

# if more than one argument, merge into string
merged : str = ""
for i in range(1, n):
    merged += " " + sys.argv[i]

# reverse string
reverse : str = merged[:0:-1]

# switch letter case
swcase : str = reverse.swapcase()

print(swcase)
kata :str = "The right format"

# pad out the front of the string with dashes so it matches 42 characters
kata :str = "-" * (41 - len(kata)) + kata

print(kata)
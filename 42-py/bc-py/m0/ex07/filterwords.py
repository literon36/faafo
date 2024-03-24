import sys
import string

# check if two arguments are provided, the second one being a number
if not len(sys.argv) == 3 or not sys.argv[2].isdigit():
    print("ERROR")
    sys.exit(1)

# convert the second argument to an integer
n :int = int(sys.argv[2])

# remove all punctuiation from the first argument
text :str = sys.argv[1].translate(str.maketrans("", "", string.punctuation))

# split the text into words
words :list[str] = text.split()

# print(words)

# filter the words
filtered_words :list[str] = [word for word in words if len(word) > n]

print(filtered_words)
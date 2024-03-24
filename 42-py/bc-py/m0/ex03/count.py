import sys
import string # for punctuation counting

def text_analyzer(text = None) -> None:
    """
    Prints the number of characters, spaces, uppercase, lowercase
    and punctuation characters in a text
    """

# if None or an empty string is provided, the user is prompted to provide a string
    if text is None or text == "":
        text = input("What is the text to analyse?\n")

# if the argument is not a string, an error message is printed
    elif not isinstance(text, str):
        print("The argument must be a string")
        sys.exit(1)

# count upper case characters
    upper : int = 0
    for c in text:
        if c.isupper():
            upper += 1

# count lower case characters
    lower : int = 0
    for c in text:
        if c.islower():
            lower += 1

# count punctuation using string.punctuation
    punctuation : int = 0
    for c in text:
        if c in string.punctuation:
            punctuation += 1

# count spaces
    spaces : int = 0
    for c in text:
        if c == " ":
            spaces += 1

# print results
    print("The text contains {} character(s)".format(len(text)))
    print("  - {} upper letter(s)".format(upper))
    print("  - {} lower letter(s)".format(lower))
    print("  - {} punctuation mark(s)".format(punctuation))
    print("  - {} space(s)".format(spaces))

# when standalone, call the function
if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Error: too many arguments")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()
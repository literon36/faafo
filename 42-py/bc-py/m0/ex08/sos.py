import sys

# if no arguments are provided, print usage
if len(sys.argv) == 1:
    print("Usage: python sos.py <string>")
    sys.exit()

# merge all arguments into one string
merged :str = " ".join(sys.argv[1:])
print(merged)

# check if merged is alpanumeric
if not merged.replace(" ", "").isalnum():
    print("ERROR")
    sys.exit(1)

# convert to uppercase
upper :str = merged.upper()

morse :dict[str, str] = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    "0" : "-----",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    " " : "/"
}

# convert to morse code
morsecode :str = ""
for c in upper:
    morsecode += morse[c] + " "

print(morsecode)
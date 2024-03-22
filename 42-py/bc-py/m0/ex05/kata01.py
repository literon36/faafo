kata :dict[str, str] = {
    "Python" : "Guido van Rossum",
    "Ruby" : "Yukihiro Matsumoto",
    "PHP" : "Rasmus Lerdorf"
}

for lang, name in kata.items():
    print(lang + " was created by " + name)
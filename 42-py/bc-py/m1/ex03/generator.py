import random
from typing import Generator

def shuffle_list(li :list) -> list:
    for i in range(len(li)-1, 0, -1):
        j = random.randint(0, i)
        li[i], li[j] = li[j], li[i]
    return li

def generator(text :str, sep=" ", option=None) -> Generator[str, None, None]:
    ''' Splits the text according to the sep value and yields the substrings.
        Option precise if a action is performed to the substrings before it is yielded.
    '''
    words :list[str] = text.split(sep)
    
    if option == "shuffle":
        words = shuffle_list(words)
    elif option == "unique":
        words = list(set(words))
    elif option == "ordered":
        words.sort()

    yield from words


if __name__ == "__main__":
    text = "Le Lorem Ipsum est simplement du faux texte. Lorem Ipsum est..."
    for word in generator(text, sep=" "                   ):  print(word); print("=" * 10)
    for word in generator(text, sep=" ", option="shuffle" ):  print(word); print("=" * 10)
    for word in generator(text, sep=" ", option="ordered" ):  print(word); print("=" * 10)
    for word in generator(text, sep=" ", option="unique"  ):  print(word)
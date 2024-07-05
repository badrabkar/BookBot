
import os

def main():
    path_to_file = "/Users/babkar/goinfre/BookBot/books/frankenstein.txt"
    filename = os.path.basename(path_to_file)
    content = read_file(path_to_file)
    size = countWords(content)
    dictionary = countCharacters(content)
    dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}

    print("--- Begin report of " + filename + " ---")
    print(str(size) + " words found in the document\n")

    for key in dictionary.keys():
        string = "\\n" if key == '\n' else str(key)
        print('The "' + string + '"' + " character was found " + str(dictionary[key]) + " times")

def read_file(path_to_file : str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def countWords(content: str) -> int:
    words = content.split()
    return len(words)

def countCharacters(content: str) -> dict[int, int]:
    hashmap = {}
    content = content.lower()

    for c in content:
        if c == ' ':
            continue
        if  c not in hashmap:
            hashmap[c] = 0
        hashmap[c] += 1
    return hashmap



main()
from stats import wordcount
from stats import charcount
def get_book_text(filepath):
    with open(filepath) as f:
        fileContents = f.read()
        return fileContents
def main():
    print("============ BOOKBOT ============")
    filepath = "books/frankenstein.txt"
    wordnum = get_book_text(filepath)
    print(f"Bookbot analysing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {wordcount(wordnum)} total words")
    print("--------- Character Count -------")
    for char in charcount(wordnum):
        cunt = charcount(wordnum)[char]
        print(f"{char}: {cunt}")
    print("============= END ===============")
main()
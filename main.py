from stats import wordcount
from stats import charcount
def get_book_text(filepath):
    with open(filepath) as f:
        fileContents = f.read()
        return fileContents
def main():
    filepath = "books/frankenstein.txt"
    wordnum = get_book_text(filepath)
    print(f"{wordcount(wordnum)} words found in the document")
    print(charcount(wordnum))
main()
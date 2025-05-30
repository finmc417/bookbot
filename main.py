from stats import wordcount
from stats import charcount
import sys
if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(filepath):
    with open(filepath) as f:
        fileContents = f.read()
        return fileContents
def main():
    print("============ BOOKBOT ============")
    filepath = sys.argv[1]
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
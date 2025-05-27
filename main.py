def get_book_text(filepath):
    with open(filepath) as f:
        fileContents = f.read()
        return fileContents
def wordcount(text):
    words = text.split()
    return len(words)
def main():
    filepath = "books/frankenstein.txt"
    print(f"{wordcount((get_book_text(filepath)))} words found in the document")
main()
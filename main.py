def get_book_text(filepath):
    with open(filepath) as f:
        fileContents = f.read()
        return fileContents
def main():
    filepath = "books/frankenstein.txt"
    print(get_book_text(filepath))
main()
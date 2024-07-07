def main():
    text = get_book_text("books/frankenstein.txt")
    print(count_words(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(str):
    return len(str.split())

main()

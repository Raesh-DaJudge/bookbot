def main():
    text = get_book_text("books/frankenstein.txt")
    print(count_words(text))
    print(count_characters(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(str):
    return len(str.split())

def count_characters(str):
    chars = {}
    
    text = str.lower()
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    
    return chars

main()

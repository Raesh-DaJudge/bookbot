def main():
    print_report("books/frankenstein.txt")

def print_report(path):
    text = get_book_text(path)
    print(f"--- Begin report of {path} ---")
    print(count_words(text))

    chars = count_characters(text)
    sorted_chars = sorted(chars, key=chars.get, reverse=True)
    for key in sorted_chars:
        if key.isalpha():
            print(f"The '{key}' character was found {chars[key]} times")

    print("--- End report ---")

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

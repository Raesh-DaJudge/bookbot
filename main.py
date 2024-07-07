def main():
    print_report("books/frankenstein.txt")

def print_report(path):
    text = get_book_text(path)
    print(f"--- Begin report of {path} ---")
    print(count_words(text))
    print()

    chars = count_characters(text)
    sorted_chars = chars_dict_to_sorted_list(chars)
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")

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


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()

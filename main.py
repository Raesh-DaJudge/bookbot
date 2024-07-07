def main():
    with open("books/frankenstein.txt") as f:
        content = f.read()
        words = len(content.split())
        print(words)



main()

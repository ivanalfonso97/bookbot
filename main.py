from stats import get_num_words, get_num_chars
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    with open(book_path) as file:
        book_text = file.read()

    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in num_chars:
        if item["char"]:
            print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")  
    
main()
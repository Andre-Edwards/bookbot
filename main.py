from stats import get_word_count, get_characters, get_book_text
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = get_word_count(text)
    characters = get_characters(text)

    print("============ BOOKBOT ============")
    print(F"Analayzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    sorted_characters = sorted(characters.items(), key=lambda item: item[1], reverse=True)
    
    print("--------- Character Count -------")
    for char, count in sorted_characters:
        print(f"{char}: {count}")
    print("============= END ===============")


main()
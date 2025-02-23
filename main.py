from stats import get_word_count, get_characters, get_book_text
def main():
    book_path = "books/frankenstein.txt"
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
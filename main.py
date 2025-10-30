import sys
from stats import get_num_words, get_char_count, print_sort_dics

def main():
    try:
        path_to_file = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(path_to_file)} total words")
        print("--------- Character Count -------")
        print_sort_dics(get_char_count(path_to_file))
        print("============= END ===============")
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return

main()



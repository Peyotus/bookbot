def get_num_words(path):
    with open(path) as f:
        file_contents = f.read()
        word_list = []
        word_list = file_contents.split()
        count = 0
        for word in word_list:
            count += 1
        print(f"Found {count} total words")
    return



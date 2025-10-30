def get_num_words(path):
    with open(path) as f:
        file_contents = f.read()
        word_list = file_contents.split()
        count = 0
        for word in word_list:
            count += 1
    return count

def get_char_count(path):
    with open(path) as f:
        file_contents = f.read()
        word_list = file_contents.split()
        char_dic = dict()
        for word in range (0, len(word_list)):
            letters = list(word_list[word])
            for l in letters:
                lwr = l.lower()
                if lwr in char_dic:
                    char_dic[lwr] += 1
                else:
                    char_dic[lwr] = 1
    return char_dic

def sort_on(items):
    return items["num"]


def print_sort_dics(unsorted_dic):
    new_list = []
    for key in unsorted_dic:
        if key.isalpha():
            char = key
            num = unsorted_dic[key]
            dic = {"char": char, "num": num}
            new_list.append(dic)
    new_list = sorted(new_list, reverse=True, key=sort_on)
    for list_item in new_list:
        print(f"{list_item["char"]}: {list_item["num"]}")
    return



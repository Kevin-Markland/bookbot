def word_count(some_string):
    word_list = some_string.split()
    word_list_len = len(word_list)
    print(f"Found {word_list_len} total words")

def char_counter(string_to_count):
    all_chars = {}
    for char in string_to_count:
        c = char.lower()
        all_chars[c] = all_chars.get(c, 0) + 1
    return all_chars

def sort_on(dict):
    return dict["num"]

def dict_sorter(some_dict):
    sorter = []
    for key,val in some_dict.items():
        if not key.isalpha():
            continue
        sorter.append({"char": key, "num": val})
    
    sorter.sort(reverse=True, key=sort_on)
    return sorter


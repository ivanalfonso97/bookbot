def sort_on(dict):
    return dict["count"]

def sort_num_chars(chars_dict):
    char_list = []
    for key in chars_dict:
        char_list.append({
            "char": key,
            "count": chars_dict[key]
        })
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def get_num_words(book_text):
    word_list = book_text.split()
    num_words = len(word_list)
    return num_words

def get_num_chars(book_text):
    char_counts = {}
    for char in book_text:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char in char_counts:
                char_counts[lower_char] += 1
            else:
                char_counts[lower_char] = 1
    sorted_char_list = sort_num_chars(char_counts)
    return sorted_char_list
stop = ['Python', 'php', 'go', 'C']

phrase = 'языки программирования и прочее: Python php go A B C'


def no_stop_words(string, stop_word):
    string_no_comma = list(filter(lambda x: x != ',', string))
    phrase_upper_list = ''.join(list(map(lambda x: x.upper(), string_no_comma))).split(' ')
    stop_upper_list = list(map(lambda x: x.upper(), stop_word))
    some_list = []
    for item in phrase_upper_list:
        if item not in stop_upper_list:
            some_list.append(item)
    return ''.join(some_list)


print(no_stop_words(phrase, stop))

def add_word(words_list): #영단어랑 뜻 딕셔너리 형태로 저장함.
    while True:
        a = input('word: ')
        if a == 'exit':
            break
        b = input('meaning: ')
        if b == 'exit':
            break
        words_list[a] = b

def show_wordbook(words_list):
    print(words_list)

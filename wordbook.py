import json
import random

def input_word(): #영단어랑 뜻 딕셔너리 형태로 저장함.

    word = {}
    while True:
        input_word = input('>> ')
        if input_word.strip().lower() == '!exit':
            break
        save_word = input_word.split(',')

        if len(save_word) !=2 or input_word.strip().lower() == ',':
            print('단어 저장 실패. 형식을 다시 확인해주세요.')
            continue
        if save_word[0] in ' '  or save_word[1] in ' ':
            print('**단어는 공백일 수 없습니다**')
            continue
        elif not save_word[0] or not save_word[1]:
            print('단어를 입력하세요')
            continue
        try:
            word[save_word[0].strip().lower()] = save_word[1].strip().lower()
        except:
            print('단어 저장 실패. 형식을 다시 확인해주세요.')
    print('\n[단어 확인]')
    for i in word:
        print(f"{i}, {word[i]}")
    while True:
        modify = list(input("오류가 있는 단어는 삭제하세요(삭제할 영단어만 입력, 여러 개 입력 가능, 없으면 엔터): ").split(','))
        for j in modify:
            try: 
                del word[j.strip()]
                print(f'{j.strip()}단어 삭제 성공 :)')
            except:
                print(f'{j.strip()}단어 삭제 실패 :(')
        while True:
            end = input('단어 삭제를 완료하시겠습니까?(Y/N) : ')
            if end.lower().strip() == 'y' or end.lower().strip() == 'n':
                break
            else:
                print("**형식에 맞게 다시 입력해주세요**")
                continue

        if end.lower().strip() == 'y':
            break
        else:
            continue


#단어장 생성 or 업데이트        
    while True:
        answer = input('단어장 파일을 생성하셨나요?: Y/N ').strip().upper()
        if answer != 'Y' and answer != 'N':
            print('형식에 맞게 입력해주세요')    
            continue
        else:
            break
    if answer == 'Y':
        while True:
            note_path = input('파일명을 입력하세요(\'파일명.json\'의 형태로 입력하세요):').strip()
            if note_path[-5:] != '.json':
                print('파일명 작성법을 지키세요!!')
                continue
            try:
                with open(note_path, "r", encoding="utf-8") as f:
                    pass
            except FileNotFoundError:
                print('단어장이 존재하지 않습니다.\n')
                answer_1 = input('다시 입력하시겠습니까? Y/N').strip().upper()
                if answer_1 == 'Y':
                    continue
                elif answer_1 == 'N':
                    print('단어 입력을 종료합니다, 메인 화면으로 돌아갑니다.')
                    return

            update_wordbook(word, note_path)
            return

    elif answer == 'N':
        while True:
            note_path = input('생성할 파일명을 입력하세요(\'파일명.json\'의 형태로 입력하세요):').strip()
            if note_path[-5:] != '.json':
                print('파일명 작성법을 지키세요!!')
                continue

            try:
                with open(note_path, "r", encoding="utf-8") as f:
                    print("**파일이 이미 존재합니다. 파일명을 다시 입력해주세요**")
                    continue
            except FileNotFoundError:
                pass

            with open(note_path, "w", encoding="utf-8") as f:
                json.dump(word, f, ensure_ascii=False, indent=4)
            return


def update_wordbook(word_list, file_path):
#이전 단어 불러오기     
    with open(file_path, "r", encoding="utf-8") as f:
        past_word = json.load(f)

#새로운 단어들과 이전 단어들 간 중복 단어 제거 
    overlap_dict = [word_list, past_word]
    pair_set = set()
    for d in overlap_dict:
        pair_set.update(d.items())
    
#단어 업데이트   
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(dict(pair_set), f, ensure_ascii=False, indent=4)
    return

def show_wordbook(num_of_word):
     while True:
    #파일 열기
        note_path = input('파일명을 입력하세요(\'파일명.json\'의 형태로 입력하세요):').strip()
        if note_path[-5:] != '.json':
            print('파일명 작성법을 지키세요!!')
            continue
    #파일 존재 유무 검사        
        try:
            with open(note_path, "r", encoding="utf-8") as f:
                show_word = json.load(f)
        except FileNotFoundError:
            print('파일이 존재하지 않습니다')
            return 'null' 
    #값 반환
        number = len(show_word)
        if number == 0:
            print('단어장이 비어있습니다')
            return {}
        if num_of_word > number:
            print(f'불러올 단어가 너무 많습니다. 현재 {number}개의 단어가 저장되어 있습니다.')
            return {}
        else:
            return dict(random.sample(list(show_word.items()), num_of_word))

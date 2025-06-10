import pandas as pd
from wordbook import *
def pick_up_word(answer, num):
    level = ['all','초등', '중고', '전문']
    picked_word ={}
    if not answer in level:
        return picked_word  
    #all = 3000, 초등 = 800, 중고 = 1800, 전문 = 400
    for i in level:
        if answer == i:
            df = pd.read_csv(f'word_pack/words_pack_grade_{i}.csv')
            num = min(num, len(df))
            sampled_df = df.sample(num)
            picked_word = dict(zip(sampled_df['단어'], sampled_df['뜻']))
            return picked_word

def append_picked_word(picked_word):
    answer = input('단어장 파일을 생성하셨나요?: Y/N ').strip().upper()
        
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
                    print('단어 입력을 종료합니다')
                    return          
            update_wordbook(picked_word, note_path)
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
                json.dump(picked_word, f, ensure_ascii=False, indent=4)
            return    
    
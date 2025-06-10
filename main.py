from wordbook import *
from game import *
from wordpack import *
from LLM import *

def main():
    show_word = {}
    while True:

        print('\n기능 선택\n' \
        '1.단어 저장\n' \
        '2.단어장\n' \
        '3.게임\n' \
        '4.예문 학습\n'\
        '5.나가기\n') 

        a = input("1, 2, 3, 4 입력: ")

        #형변환 점검       
        try:
            answer = int(a)
        except ValueError:
            print("1 이상 4 이하 정수 값 하나만 입력하세요!")
            continue

        if answer == 1:
            print('단어를 입력하세요(언제든 \'!exit\'를 입력해 단어 입력을 끝낼 수 있습니다.)\n**\'단어, 뜻\'의 형태로 입력하세요**')
            input_word()
            continue    

        elif answer == 2:
            choice = input('나의 단어장 불러오기(\'my\') / 프로그램 단어 불러오기(\'pack\'): ').strip().lower()
            if choice == 'my':
                while True:
                    try:
                        num = int(input('불러올 단어의 갯수를 입력하세요: '))
                    except ValueError:
                        print('자연수 값을 넣으세요!')
                        continue
                    show_word = show_wordbook(num)
                    if not show_word:
                        kdic = input('종료하시겠습니까?: Y/N ').strip().upper()
                        if kdic == 'Y':
                            break
                        elif kdic == 'N':
                            continue
                    
                    print(show_word)
                    break
            elif choice == 'pack':
                while True:
                    answer_2= input('단계 선택(all, 초등(800개), 중고(1800개), 전문(400개)): ')
                    try:
                        number = int(input('\n**최대 갯수 초과 입력 시 최대 갯수 출력** \n단어 개수: '))
                    except:
                        print('자연수 값을 넣으세요!\n')
                        continue
                    show_word = pick_up_word(answer_2, number) 
                    if not show_word:
                        print('단계를 다시 선택하세요!\n')
                        continue
                    else:
                        print(f"{'[단어]':13s}{'[의미]'}")
                        for words in show_word:
                            print(f"{words:14s}: {show_word[words]}")
                        print('\n')
                        append_picked_word(show_word)
                        break
            continue

        elif answer == 3:
            if not show_word:
                print('**단어를 먼저 불러오세요**')
                continue
            else:
                play_game(show_word)
                continue
        elif answer == 4:
            generate_sentence()
        # 단어 입력 받고 만들어 놓은 make_sentence()함수에 인자로 넣어서 LLM딸깍
        # 해당 함수는 LLM 모듈에서 불러 올게용


        elif answer == 5:
            print('프로그램을 종료합니다')
            return 
        else:
            print("1과 5사이의의 정수 값 하나만 입력하세요!")
            continue

    # 단어 저장 = add_word() 불러오고, 단어장 = show_word() 불러오고, 
    # 게임 = play_game()불러오고, 나가기 = 나갔다는 문구랑 함께 main.py종료 할 수 있게 plz

if __name__ == "__main__":
   main()

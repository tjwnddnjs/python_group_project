from wordbook import *
from game import *
from pathlib import Path


def main():
    show_word = {}
    while True:
          
        print('기능 선택\n' \
        '1.단어 저장\n' \
        '2.단어장\n' \
        '3.게임\n' \
        '4.나가기\n') 
    
        a = input("1, 2, 3, 4 입력: ")

        #형변환 점검       
        try:
            answer = int(a)
        except ValueError:
            print("1 이상 4 이하 정수 값 하나만 입력하세요!")
            continue
    
        if answer == 1:
            print('단어를 입력하세요(언제든 \'exit\'를 입력해 단어 입력을 끝낼 수 있습니다.)\n')
            input_word()
            continue

        elif answer == 2:
            while True:
                num = int(input('불러올 단어의 갯수를 입력하세요: '))
                show_word = show_wordbook(num)
                if not show_word:
                    if input('종료하시겠습니까?: Y/N ').strip().upper() == 'Y':
                        break
                    continue
                else:
                    print(show_word)
                    break
            continue
        
        elif answer == 3:
            if not show_word:
                print('단어장을 먼저 불러오세요')
                continue
            else:
                play_game(show_word)
                continue

        elif answer == 4:
            print('프로그램을 종료합니다')
            return 
        else:
            print("1 이상 4 이하 정수 값 하나만 입력하세요!")
            continue

    # 단어 저장 = add_word() 불러오고, 단어장 = show_word() 불러오고, 
    # 게임 = play_game()불러오고, 나가기 = 나갔다는 문구랑 함께 main.py종료 할 수 있게 plz

if __name__ == "__main__":
	main()


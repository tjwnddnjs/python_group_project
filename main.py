from wordbook import *
from game import *
# from LLM import *
words = {}
add_world(words) #wordbook 함수, 직접 써서 추가. 아무때나 exit쓰면 나와짐. 
# generate_words('대학교', words) #LLM 써서 단어 30개 무작위 생성/ 이거 오류 많이 남ㅠㅠ
# print(words) #잘 써지나 확인

play_game(words)

# generate_words('대학교', words) #LLM 써서 단어 30개 무작위 생성/ 이거 오류 많이 남ㅠㅠ
print(words) #잘 써지나 확인

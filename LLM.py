from openai import OpenAI
import re
def generate_sentence():
    while True:
        example_word = input('학습할 단어를 입력하세요.(학습 종료:!exit) :').strip().lower()
        if example_word == '!exit':
            break
        while True:
            study_answer = input(f"{example_word}에 대한 학습 진행 Y/N: ").strip().lower()
            if study_answer == 'n':
                break

            elif study_answer == 'y' :
                client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key="",
                )

                completion = client.chat.completions.create(
                model="deepseek/deepseek-r1-0528-qwen3-8b:free",
                messages=[
                    {
                    "role": 'system',
                    "content": f"""
                    1. {example_word}에 대한 단어 뜻과 예시 문장을 출력해. 
                    만약 {example_word}가 존재하지 않는 단어라면 "존재하지 않는 단어입니다."라는 메세지를 출력해
                    2. 형식 
                    {example_word} : {example_word}의 한글 번역역
                    {example_word}에 대한 영어로 된 예시 문장 1개
                    {example_word}에 대한 한글로 된 해석 문장 1개
                    **예시 문장을 생성할 때, 문장에 사용되는 총 단어수 가 20개를 넘지 않게 해.**
                    3. 2번 형식에서 작성한 형식 내 내용 외 다른 문장은 일절 출력하지마. 대답도 하지마.

                    """ 
                    }
                ]
                )
                lines =completion.choices[0].message.content.strip().split('\n')
                
                if len(lines) != 3: # 3줄 출력 아니면 일단 거르고 봄.
                    print('LLM 모델의 비정상적 작동에 의해 중지되었습니다. 다시 시도해주세요.')
                
                elif re.search(r'[가-힣]', lines[1]): # 두 번째 줄에 한글 포함 = 거름
                    print('LLM 모델의 비정상적 작동에 의해 중지되었습니다. 다시 시도해주세요.')
                elif re.search(r'[a-zA-Z]', lines[2]): # 세 번째 줄에 영어 포함 = 거름
                    print('LLM 모델의 비정상적 작동에 의해 중지되었습니다. 다시 시도해주세요.')
                
                else:
                    print('\n'+'-'*40+'\n'+completion.choices[0].message.content+'\n'+'-'*40+'\n')

                break
            else:
                print("다시 입력해 주세요")
                continue


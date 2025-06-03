from openai import OpenAI
import json
def generate_sentence():
    while True:
        example_word = input('학습할 단어를 입력하세요.(학습 종료:exit) :').strip().lower()
        if example_word == 'exit':
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
                    2. 형식 
                    {example_word} : **{example_word}의 단어 뜻**
                    {example_word}에 대한 영어로 된 예시 문장 1개
                    {example_word}에 대한 한글로 된 해석 문장 1개
                    **예시 문장을 생성할 때, 문장에 사용되는 총 단어수 가 20개를 넘지 않게 해.**
                    3. 2번 형식에서 작성한 형식 내 내용 외 다른 문장은 일절 출력하지마. 대답도 하지마.

                    """ #프롬프트 다시 손 봐야함.
                    }
                ]
                )
                print('\n'+'-'*40+'\n'+completion.choices[0].message.content+'\n'+'-'*40+'\n')
                # print('우리 LLM 정상 영업 합니다.')

                break
            else:
                print("다시 입력해 주세요")
                continue

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
                # client = OpenAI(
                # base_url="https://openrouter.ai/api/v1",
                # api_key="",
                # )

                # completion = client.chat.completions.create(
                # model="deepseek/deepseek-r1-0528-qwen3-8b:free",
                # messages=[
                #     {
                #     "role": 'system',
                #     "content": f"""
                #     {example_word}에 대해 단어 뜻과 예문, 뜻을 출력. 
                #     """ #프롬프트 다시 손 봐야함.
                #     }
                # ]
                # )
                # print(completion.choices[0].message.content)
                print('우리 LLM 정상 영업 합니다.')

                break
            else:
                print("다시 입력해 주세요")
                continue

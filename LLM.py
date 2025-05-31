import requests
import json

def generate_words(level,words_list): 
    # level엔 '대학생', '대학원생' 같은 문자열이 들어가고, 
    # words_list 자리엔 main에서 선언해놓은 words 딕셔너리가 들어감.
    # ??수준의 영단어 30개를 생성해서 기존의 딕셔너리에 넣는 함수
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "", #api key 는 항상 지우고 깃허브 올리기
        "Content-Type": "application/json"
    },
    data=json.dumps({
        "model": "meta-llama/llama-3.3-8b-instruct:free", #모델은 아무거나 설정해도 ㄱㅊㅊ
        "messages": [{
            'role' : 'system',
            'content' : f"""
            1. {level} 어휘 수준의 단어를 추천해줘.
            2. 30개의 단어를 추천해줘.
            3. 출력은 **반드시** 아래 JSON 스키마로만 구성하고, 그 외 코멘트나 텍스트를 생성하지 마.
            **JSON 스키마**:
            {{
            "<영어단어1>":"<한글뜻1>",
            "<영어단어2>":"<한글뜻2>",
            … (총 30개)
            }} 
            **{{내용}}의 형태여야해** 
            4. {words_list} 단어는 추천에서 제외해줘.
""" #나중에 보면 알겠지만 LLM자체가 문제가 있음. 그래서 json형태로 반환을 안해줘서 아래에서 오류가 발생함.
        }]
        
    })
    )

    if response.status_code != 200:
        print('error')
    
    res_con = response.json()['choices'][0]['message']['content']
    try:
        data = json.loads(res_con)
    # 오류가 여기서 발생함. 얘가 마지막에 중괄호 {} 를 안써서 딕셔너리로 안바뀐다던지 
    # 가끔씩 콤마 , 를 까먹는다던지 해서 이거 좀 문제임 loads가 안됨ㅠㅠㅠ

        for key, value in data.items():
            words_list[key] = value
    except json.JSONDecodeError: 
            print("파싱 에러, 원본 응답:\n", res_con)

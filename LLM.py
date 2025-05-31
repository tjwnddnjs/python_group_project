from openai import OpenAI
import json
def generate_words(level,words_list):
        
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    )

    completion = client.chat.completions.create(
    model="deepseek/deepseek-r1-0528-qwen3-8b:free",
    messages=[
        {
        "role": 'system',
        "content": f"""
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
    """
        }
    ]
    )
    a = completion.choices[0].message.content

    start = a.find('{')
    end   = a.rfind('}')

    # 유효 인덱스 검사 후 슬라이싱
    if start != -1 and end != -1 and start < end:
        json_str = a[start:end+1]
    else:
        json_str = ''
    print(json_str)
    try:
        data= json.loads(json_str)
    except:
        print('조졌네네')
        pass

    print(data,type(data))
generate_words('대학생', {})
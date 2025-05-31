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
                1. recommend English words for {level} students.
                2. recommend 30 words.
                3. **make sure** the output is in a **Python dictionary data type**, Don't generate any other comments or text.
                **Python dictionary data type**:
                {{
                  "English word 1" : "Korean meaning of English word 1",
                  "English word 2" : "Korean meaning of English word 3",...
                  "English word 30" : "Korean meaning of English word 30"
                }} 
                4. exclude {words_list} from the recommendation.
    """
        }
    ]
    )
    a = completion.choices[0].message.content

    word_dict = json.loads(a)
    print(word_dict)
generate_words('대학생', {})
    # start = a.find('{')
    # end   = a.rfind('}')

#     # 유효 인덱스 검사 후 슬라이싱
#     if start != -1 and end != -1 and start < end:
#         json_str = a[start:end+1]
#     else:
#         json_str = ''
#     print(json_str)
#     try:
#         data= json.loads(json_str)
#     except:
#         print('조졌네네')
#         pass

#     print(data,type(data))
# generate_words('대학생', {})
import pandas as pd
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


    
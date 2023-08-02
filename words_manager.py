import pandas as pd
import random

# df = pd.read_csv("data/french_words.csv")
#
# current_word = df.sample()
# print(current_word)
# print(current_word['French'].to_string(index=False))
# print(current_word['English'].to_string(index=False))
# index = current_word.index
# print(index)
# to_learn = df
#
# print(len(to_learn))
#
# # print(df.index[current_word])
# # index = to_learn[to_learn['French'] == current_word['French']].index.values
# # print(index)
#
# # print(df.loc[current_word])
#
# to_learn.drop(index=index)

d = {'French': ['yay'], 'English': ['you win']}
current_word = pd.DataFrame(data=d)

print(current_word)


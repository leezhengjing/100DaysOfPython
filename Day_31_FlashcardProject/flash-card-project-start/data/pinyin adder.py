import pandas
import pinyin_jyutping_sentence

data = pandas.read_csv("chinese_words.csv")
word_list = data["Chinese"].to_list()

pinyin_list = []
for word in word_list:
    new_word = pinyin_jyutping_sentence.pinyin(word)
    pinyin_list.append(new_word)

print(pinyin_list)

data["pinyin"] = pinyin_list

data.to_csv("final_chinese_words.csv")
from typing import List
from keras.preprocessing.text import Tokenizer
import io
import json


def getArray(path: str) -> List[List[str]]:
    articleList = []
    with open(path) as textFile:
        tempList: List[str] = textFile.readlines()
        for i, article in enumerate(tempList):
            if i == 200:
                break
            articleList.append(article.split())

    return articleList


def WordtoInt(arr: List[List[str]]):
    t = Tokenizer(num_words=500)
    t.fit_on_texts(arr)
    sequences = t.texts_to_sequences(arr)
    # print('sequences : ', sequences, '\n')
    # print('word_index : ', t.word_index)
    tokenizer_json = t.to_json()
    with io.open('tokenizer.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(tokenizer_json, ensure_ascii=False))
    # print(tokenizer_json)
    return sequences


def getSequences() -> List[List[int]]:
    arr1 = getArray('climate.txt')
    arr2 = getArray('covid-19.txt')
    arr3 = getArray('racism.txt')
    arr1 = arr1 + arr2 + arr3
    return WordtoInt(arr1)


if __name__ == "__main__":
    arr = getSequences()
    print(arr)

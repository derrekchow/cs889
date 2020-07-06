import numpy as np
from scipy.spatial import distance
import re

if __name__ != "__main__":
    words = np.load('data/words.npy')
    vectors = np.load('data/vectors.npy')


def is_valid_word(word): # format: word = [<NAME>, <TYPE>]
    return word[1] not in ["propn", "num"]


def is_cleaned_data(word_name):
    # the character '-' in valid word appears at most once
    count_minus_sign = 0
    for char in word_name:
        if not char.isalpha() and char != '-':
            return False
        if char == '-':
            count_minus_sign += 1

    return (count_minus_sign == 0 or count_minus_sign == 1)


def generate_giga(): # giga has underscores
    validate_words = {}
    for word in np.loadtxt('data/glove_model.txt', usecols=0, dtype='str'):
        validate_words[word.lower()] = None
    
    data = open("data/giga_model.txt", "r")

    words = []
    vectors = []
    
    for line in data:
        row = line.split(' ')
        row[-1] = row[-1].strip()
        vector = np.array(row[1:], dtype='float')
        word = row[:1][0]
        w = word.lower().split('_')

        if (w[0] in validate_words and is_valid_word(w) and is_cleaned_data(w[0])):
            words.append(word)
            vectors.append(vector)

    np.save('data/vectors.npy', np.array(vectors))
    np.save('data/words.npy', np.array(words))


def get_word_dict():
    word_dict = {}

    for i in range(0, len(words)):
        word_dict[words[i]] = i

    return word_dict


def answer_index(vector):
    return np.argsort(
        distance.cdist([vector], vectors)
    )[0][2:12]


def add(w1, w2):
    vec_sum = vectors[w2] + vectors[w1]
    indexes = answer_index(vec_sum)
    res = []
    for i in range(0, len(indexes)):
        res.append(words[indexes[i]])
    
    return res


if __name__ == "__main__":
    generate_giga()
else:
    word_dict = get_word_dict()
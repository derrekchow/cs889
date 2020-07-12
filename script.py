import numpy as np
from scipy.spatial import distance

words = np.load('data/words.npy')
vectors = np.load('data/vectors.npy')

def get_words():
    return words

def gen_words():
    data = np.loadtxt('data/model.txt', usecols=0, dtype='str')
    np.save('data/words.npy', data)

def gen_vectors():
    data = []
    f = open("data/model.txt", "r")
    for line in f:
        row = line.split(' ')
        row[-1] = row[-1].strip()
        data.append(np.array(row[1:], dtype='float'))

    np.save('data/vectors.npy', np.array(data))

def get_words_list(words):
    words = []

    for i in range(0, len(words)):
        words.append({"name": words[i], "code": i})

    return words

def answer_index(vector, vectors):
    return np.argsort(
        distance.cdist([vector], vectors)
    )[0][2:10]

words_list = get_words_list(words)

def add(w1, w2):
    vec_sum = vectors[w2] + vectors[w1]
    indexes = answer_index(vec_sum, vectors)
    res = []
    for i in range(0, len(indexes)):
        res.append(words[indexes[i]])
    
    return res

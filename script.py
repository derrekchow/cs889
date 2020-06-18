import numpy as np
from scipy.spatial import distance

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


def get_words(words):
    word_dict = {}

    for i in range(0, len(words)):
        word_dict[words[i]] = i

    return word_dict

def answer_index(vector, vectors):
    return np.argsort(
        distance.cdist([vector], vectors)
    )[0][2:10]


def main():
    words = np.load('data/words.npy')
    vectors = np.load('data/vectors.npy')
    word_dict = get_words(words)

    w1 = input("Word 1: ")
    w2 = input("Word 2: ")
    if (w1 in word_dict) and (w2 in word_dict):
        vec_sum = vectors[word_dict[w2]] + vectors[word_dict[w1]]
        indexes = answer_index(vec_sum, vectors)
        for i in range(0, len(indexes)):
            print(str(i) + ": " + str(words[indexes[i]]))

main()

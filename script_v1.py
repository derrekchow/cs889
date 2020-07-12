import numpy as np
from scipy.spatial import distance

if __name__ != "__main__":
    words = np.load('data/words.npy')
    vectors = np.load('data/vectors.npy')


def is_valid_word(word): # format: word = [<NAME>, <TYPE>]
    return len(word) > 1 and word[1] not in ["propn", "num"]

# def generate_glove(): # giga has underscores
#     validate_words = {}
#     for word in np.loadtxt('data/giga_model.txt', usecols=0, dtype='str'):
#         w = word.lower().split('_')
#         if (is_valid_word(w)):
#             validate_words[w[0]] = None
    
#     data = open("data/glove_model.txt", "r")

#     words = []
#     vectors = []
    
#     for line in data:
#         row = line.split(' ')
#         row[-1] = row[-1].strip()
#         vector = np.array(row[1:], dtype='float')
#         word = row[:1][0].lower()
        
#         if (word in validate_words):
#             words.append(word)
#             vectors.append(vector)

#     np.save('data/vectors.npy', np.array(vectors))
#     np.save('data/words.npy', np.array(words))


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
        word = row[:1][0].lower()
        w = word.split('_')

        if (w[0] in validate_words and is_valid_word(w)):
            words.append(word)
            vectors.append(vector)

    np.save('data/vectors.npy', np.array(vectors))
    np.save('data/words.npy', np.array(words))


def get_words_list():
    words_list = []

    for i in range(0, len(words)):
        w = words[i].split('_')
        words_list.append({"label": w[0], "type": w[1], "code": i})

    return words_list


def answer_index(vector):
    return np.argsort(
        distance.cdist([vector], vectors)
    )[0][2:7]


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
    words_list = get_words_list()
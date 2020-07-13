import numpy as np
from scipy.spatial import distance
from datetime import datetime

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
        word = row[:1][0].lower()
        w = word.split('_')

        if (w[0] in validate_words and is_valid_word(w) and is_cleaned_data(w[0])):
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
    )[0][2:20]


def add(w1, w2):
    vec_sum = vectors[w2] + vectors[w1]
    indexes = answer_index(vec_sum)
    res = []
    word1, word2 = words[w1].split('_')[0], words[w2].split('_')[0]
    for i in range(0, len(indexes)):
        tmp_word = words[indexes[i]].split('_')[0]
        if len(res) == 5:
            break
        if tmp_word == word1 or tmp_word == word2:
            continue
        res.append(tmp_word)

    log(words[w1], words[w2], res)
    
    return res


def log(w1, w2, ans):
    f=open("log.tsv", "a+")
    f.write(
        str(datetime.now()) + '\t' + w1.split('_')[0] + '\t' + w1.split('_')[1] + '\t' + w2.split('_')[0] + '\t' + w2.split('_')[1] + '\t' + '\t'.join(ans) + '\n'
    )
    f.close()


if __name__ == "__main__":
    generate_giga()
else:
    words_list = get_words_list()
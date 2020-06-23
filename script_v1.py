import numpy as np
from scipy.spatial import distance

def gen_words():
    data = np.loadtxt('./giga_model.txt', usecols=0, dtype='str')
    np.save('./words.npy', data)


def gen_vectors():
    data = []
    f = open("./giga_model.txt", "r")
    for line in f:
        row = line.split(' ')
        row[-1] = row[-1].strip()
        data.append(np.array(row[1:], dtype='float'))

    np.save('./vectors.npy', np.array(data))


def word_validation():
    data = np.loadtxt('./glove_model.txt', usecols=0, dtype='str')
    np.save('./words_validate.npy', data)


def get_words(words, validate_words):
    word_dict = {}
    validate = {}
    for i in range(0, len(words)):
        word_dict[words[i]] = i

    for i in range(len(validate_words)):
    	validate[validate_words[i]] = i

    return word_dict, validate


def answer_index(vector, vectors):
    return np.argsort(
        distance.cdist([vector], vectors)
    )[0][2:12]


def main():
    words = np.load('./words.npy')
    vectors = np.load('./vectors.npy')
    validate = np.load('./words_validate.npy')
    word_dict, validate_words = get_words(words, validate)

    w1 = input("Word 1: ")
    w2 = input("Word 2: ")
    
    if (w1 in word_dict) and (w2 in word_dict):
        vec_sum = vectors[word_dict[w2]] + vectors[word_dict[w1]]
        indexes = answer_index(vec_sum, vectors)
        lower_w1, lower_w2 = w1.lower(), w2.lower()
        count = 0
        for i in range(len(indexes)):
        	tmp_answer = str(words[indexes[i]])
        	lower_answer = tmp_answer.lower()
        	if lower_answer == lower_w1 or lower_answer == lower_w2 or lower_answer.split("_")[0] not in validate_words:
        		continue
        	count += 1
        	print(str(count) + ": " + tmp_answer)

# gen_words()
# gen_vectors()
# word_validation()
main()

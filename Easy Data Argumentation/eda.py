import random
import re
import utils
import csv
import jpype
import json
from konlpy.tag import Kkma

kkma = Kkma()

# 한글만 남기고 나머지는 삭제
def get_only_hangul(line):
    parseText = re.compile('/ ^[ㄱ-ㅎㅏ-ㅣ가-힣]*$/').sub('', str(line))
    return parseText

########################################################################
# Synonym replacement
# Replace n words in the sentence with synonyms from wordnet
########################################################################
def synonym_replacement(words, n):
    new_words = words.copy()
    random_word_list = list(set([word for word in words]))
    random.shuffle(random_word_list)
    num_replaced = 0
    synonyms = []
    for random_word in random_word_list:
        ## 토큰화된 단어가 명사 -> get_synonyms함수를 통해 유의어 리스트 반환
        if kkma.pos(random_word).pop()[1] == 'NNG':
            print(random_word)
            synonyms = get_synonyms(random_word)
            print(synonyms)
        if len(synonyms) >= 1:
            synonym = random.choice(list(synonyms))
            new_words = [synonym if word == random_word else word for word in new_words]
            num_replaced += 1
        if num_replaced >= n:
            break

    if len(new_words) != 0:
        sentence = ' '.join(new_words)
        new_words = sentence.split(" ")
    else:
        new_words = ""
    return new_words

def get_synonyms(word):
    synomyms = []
    try:
        for syn in wordnet[word]:
            for s in syn:
                synomyms.append(s)
    except Exception:
        pass
    return synomyms

########################################################################
# Random deletion
# Randomly delete words from the sentence with probability p
########################################################################
def random_deletion(words, p):
    if len(words) == 1:
        return words

    new_words = []
    for word in words:
        r = random.uniform(0, 1)
        if r > p:
            new_words.append(word)

    if len(new_words) == 0:
        rand_int = random.randint(0, len(words) - 1)
        return [words[rand_int]]

    return new_words

########################################################################
# Random swap
# Randomly swap two words in the sentence n times
########################################################################
def random_swap(words, n):
    new_words = words.copy()
    for _ in range(n):
        new_words = swap_word(new_words)

    return new_words


def swap_word(new_words):
    random_idx_1 = random.randint(0, len(new_words) - 1)
    random_idx_2 = random_idx_1
    counter = 0

    while random_idx_2 == random_idx_1:
        random_idx_2 = random.randint(0, len(new_words) - 1)
        counter += 1
        if counter > 3:
            return new_words

    new_words[random_idx_1], new_words[random_idx_2] = new_words[random_idx_2], new_words[random_idx_1]
    return new_words

########################################################################
# Random insertion
# Randomly insert n words into the sentence
########################################################################
def random_insertion(words, n):
    new_words = words.copy()
    for _ in range(n):
        add_word(new_words)

    return new_words


def add_word(new_words):
    synonyms = []
    counter = 0
    while len(synonyms) < 1:
        if len(new_words) >= 1:
            random_word = new_words[random.randint(0, len(new_words) - 1)]
            synonyms = get_synonyms(random_word)
            counter += 1
        else:
            random_word = ""

        if counter >= 10:
            return

    random_synonym = synonyms[0]
    random_idx = random.randint(0, len(new_words) - 1)
    new_words.insert(random_idx, random_synonym)


if __name__=='__main__':
    alpha_sr = 0.1
    alpha_ri = 0.1
    alpha_rs = 0.1
    p_rd = 0.1
    num_aug = 8

    for sentence in data:
        s = utils.cleaning(sentence[0])

        ## tokenizer를 사용해서 문장을 토큰화
        res = kkma.morphs(s)

        dict = json.loads(res)
        words = []
        for pos in dict["result"]["posInfo"]:
            words.append([pos["pos"], pos["morph"]])

        words = [word for word in words if word != ""]
        num_words = len(words)

        augmented_sentences_sr = []
        augmented_sentences_ri = []
        augmented_sentences_rs = []
        augmented_sentences_rd = []
        num_new_per_technique = num_aug

        n_sr = max(1, int(alpha_sr * num_words))
        n_ri = max(1, int(alpha_ri * num_words))
        n_rs = max(1, int(alpha_rs * num_words))

        # sr
        for _ in range(num_new_per_technique):
            a_words = synonym_replacement(words, n_sr)
            augmented_sentences_sr.append(' '.join(a_words))
        
        # ri
        for _ in range(num_new_per_technique):
            a_words = random_insertion(words, n_ri)
            augmented_sentences_ri.append(' '.join(a_words))

        # rs
        for _ in range(num_new_per_technique):
            a_words = random_swap(words, n_rs)
            augmented_sentences_rs.append(" ".join(a_words))

        # rd
        for _ in range(num_new_per_technique):
            a_words = random_deletion(words, p_rd)
            augmented_sentences_rd.append(" ".join(a_words))

        augmented_sentences_sr = [get_only_hangul(sentence) for sentence in augmented_sentences_sr]
        augmented_sentences_ri = [get_only_hangul(sentence) for sentence in augmented_sentences_ri]
        augmented_sentences_rs = [get_only_hangul(sentence) for sentence in augmented_sentences_rs]
        augmented_sentences_rd = [get_only_hangul(sentence) for sentence in augmented_sentences_rd]

        # random.shuffle(augmented_sentences)

        augmented_sentences_sr = augmented_sentences_sr[:num_aug]
        augmented_sentences_ri = augmented_sentences_ri[:num_aug]
        augmented_sentences_rs = augmented_sentences_rs[:num_aug]
        augmented_sentences_rd = augmented_sentences_rd[:num_aug]

        augmented_sentences_sr.append(sentence)
        augmented_sentences_ri.append(sentence)
        augmented_sentences_rs.append(sentence)
        augmented_sentences_rd.append(sentence)
	
	path = ""
        with open(path, 'at') as out_file:
            for sen in aug_sentences_sr:
                wr = csv.writer(out_file, delimiter='\t')
                wr.writerow([sen, "label"])


 

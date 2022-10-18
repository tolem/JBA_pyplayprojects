import random, nltk

with open(input(), "r", encoding="utf-8") as f:
    words = f.read().split()
bigram_list = list(nltk.bigrams(words))
markov = dict()

for pair in bigram_list:
    head, tail = pair
    if head in markov and tail in markov[head]:
        markov[head][tail] += 1
    else:
        markov[head] = {tail: 1}
for _ in range(10):
    punctuation, sentence, end_word = [".", "!", "?"], [], ''
    while True:
        word = random.choice(words)
        if word[0].isupper() and word[-1] not in punctuation:
            sentence.append(word)
            break
    for i in range(9):
        prob_word = random.choices(list(markov[word].keys()), list(markov[word].values()))
        if i == 8:
            while len(sentence) < 4:
                word = random.choice(words)
                if word[-1] not in punctuation:
                    sentence.append(word)
            while True:
                end_word = random.choice(list(markov[word].keys()))
                if all(word[-1] not in punctuation for word in list(markov[word].keys())):
                    word = random.choice(words)
                if end_word[-1] in punctuation:
                    sentence.append(end_word)
                    break
        else:
            if prob_word[0][-1] not in punctuation:
                sentence.append(prob_word[0])
                word = prob_word[0]
    print(" ".join(sentence))

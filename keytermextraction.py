from lxml import etree
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

import nltk
import string


tree = etree.parse("news.xml")
root = tree.getroot()
lemmatizer = WordNetLemmatizer()
headlines = []
dataset = []

for title in root[0]:
    tokens = word_tokenize(title[1].text.lower())
    tagged = [nltk.pos_tag([lemmatizer.lemmatize(token)]) for token in tokens]
    exceptions = stopwords.words("english") + list(string.punctuation)
    lemmas = [word[0][0] for word in tagged if word[0][0] not in exceptions and word[0][1] == "NN"]
    headlines.append(title[0].text + ":")
    dataset.append(" ".join(lemmas))

vectorizer = TfidfVectorizer(lowercase=False)
tfidf_matrix = vectorizer.fit_transform(dataset).toarray()
terms = vectorizer.get_feature_names_out()
scores = [dict(sorted(zip(terms, s), key=lambda x: (x[1], x[0]), reverse=True)[:5]) for s in tfidf_matrix]

for headline, words in zip(headlines, scores):
    print(headline)
    print(*words.keys())

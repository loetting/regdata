from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
import os

corpus = []

for index in range(40,51):
    path = "~/Downloads/ECFR_data/ECFR-title" + str(index) + ".xml"
    with open(os.path.expanduser(path)) as file:
        corpus.append(file.read())

vectorizer = TfidfVectorizer(max_df=0.7, stop_words=ENGLISH_STOP_WORDS)
X = vectorizer.fit_transform(corpus)
corpus_stop_words = vectorizer.stop_words_.union(ENGLISH_STOP_WORDS)

stop_word_file = open('stop_words', 'w+')
for word in corpus_stop_words:
    stop_word_file.write(word + '\n')
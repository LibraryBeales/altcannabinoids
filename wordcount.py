import pandas as pd
from collections import Counter
import nltk
from nltk.corpus import words
import re

nltk.download('words')

df = pd.read_csv('redditscraper1.csv')

def clean_and_tokenize(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # Remove punctuation and numbers
    tokens = text.split()
    return tokens

english_words = set(words.words())

word_counter = Counter()

for body in df['body'].dropna():
    tokens = clean_and_tokenize(body)
    word_counter.update(tokens)

non_words = {word: count for word, count in word_counter.items() if word not in english_words}

most_common_non_words = Counter(non_words).most_common(30)

print("Ten most used words not in the English Dictionary:")
for word, count in most_common_non_words:
    print(f"{word}: {count}")
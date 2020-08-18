from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("bettor"))
print(lemmatizer.lemmatize("bettors"))
print(lemmatizer.lemmatize("best"))
print(lemmatizer.lemmatize("bests"))
print(lemmatizer.lemmatize("railroading"))
print(lemmatizer.lemmatize("geese"))

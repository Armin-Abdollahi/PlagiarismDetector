from hazm import Normalizer, word_tokenize, Stemmer, Lemmatizer

normalizer = Normalizer()
stemmer = Stemmer()
lemmatizer = Lemmatizer()

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = normalizer.normalize(text)
    return text.strip()

def tokenize_words(text: str):
    text = clean_text(text)
    return word_tokenize(text)

def stem_words(words):
    return [stemmer.stem(w) for w in words]

def lemma_words(words):
    return [lemmatizer.lemmatize(w) for w in words]

def preprocess_for_similarity(text: str) -> str:
    text = clean_text(text)
    tokens = word_tokenize(text)
    lemmas = [lemmatizer.lemmatize(t) for t in tokens]
    return " ".join(lemmas)

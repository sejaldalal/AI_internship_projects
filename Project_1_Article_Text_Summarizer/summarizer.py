import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict

# Download required NLTK resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_sentences=3):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())

    # Calculate word frequencies
    word_frequencies = defaultdict(int)
    for word in words:
        if word.isalnum() and word not in stop_words:
            word_frequencies[word] += 1

    # Score sentences
    sentences = sent_tokenize(text)
    sentence_scores = defaultdict(int)

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] += word_frequencies[word]

    # Select top sentences
    summary_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:num_sentences]

    summary = " ".join(summary_sentences)
    return summary


if __name__ == "__main__":
    with open("sample_text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    print("\n================ ORIGINAL ARTICLE ================\n")

    print(text)

    print("\n================ GENERATED SUMMARY ================\n")
    print(summarize_text(text))

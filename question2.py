import string
from collections import Counter
import spacy

def process_paragraph():
    # Load the English language model for spaCy
    nlp = spacy.load('en_core_web_sm')

    # Get paragraph input from user
    print("Enter your paragraph (press Enter twice to finish):")
    paragraph_lines = []
    while True:
        line = input()
        if line == "":
            break
        paragraph_lines.append(line)
    paragraph = "\n".join(paragraph_lines)

    # Process the paragraph with spaCy
    doc = nlp(paragraph)

    # --- First and Last Words ---
    words = [token.text for token in doc if not token.is_punct and not token.is_space]
    if not words:  # Check if paragraph was empty
        print("\nNo words found in the paragraph!")
        return
    
    print("\n--- First and Last Words ---")
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")
    print(f"Total words: {len(words)}")

    # --- Word Frequencies (lowercase, no punctuation, no stopwords) ---
    print("\n--- Word Frequencies ---")
    word_freq = Counter()
    stop_words = nlp.Defaults.stop_words

    for token in doc:
        if not token.is_punct and not token.is_space and token.text.lower() not in stop_words:
            word_freq[token.text.lower()] += 1

    if word_freq:  # Only print if we found words
        for word, count in word_freq.most_common():
            print(f"{word}: {count}")
    else:
        print("No words remaining after filtering")

    # --- Named Entities ---
    print("\n--- Named Entities ---")
    if doc.ents:
        for ent in doc.ents:
            print(f"Entity: {ent.text}, Label: {ent.label_}")
    else:
        print("No named entities found")

# Run the program
process_paragraph()
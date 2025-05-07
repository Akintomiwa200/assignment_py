def classify_words():
    
    nouns = {'dog', 'cat', 'house', 'car', 'book', 'tree', 'sun', 'water', 'computer', 'phone'}
    verbs = {'run', 'walk', 'jump', 'eat', 'sleep', 'read', 'write', 'drive', 'swim', 'talk'}

   
    sentence = input("Enter a sentence: ")

    
    words = []
    for word in sentence.split():
        word_clean = word.strip('.,!?;:"\'').lower()
        if word_clean:
            words.append(word_clean)

    
    noun_count = 0
    verb_count = 0
    unknown_count = 0

    for word in words:
        if word in nouns:
            noun_count += 1
        elif word in verbs:
            verb_count += 1
        else:
            unknown_count += 1

    
    print("\n--- Results ---")
    print(f"Total words: {len(words)}")
    print(f"Nouns: {noun_count}")
    print(f"Verbs: {verb_count}")
    print(f"Unknown words: {unknown_count}")


classify_words()
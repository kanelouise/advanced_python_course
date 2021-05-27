def collect_unique(filename):
    filename = open(f"../{filename}")
    unique_words = set()

    text = filename.read()
    words = text.split()
    for word in words:
        word = word.lower().rstrip('.,;')
        unique_words.add(word)
        sunique_words = sorted(unique_words)
    return sunique_words

from text import normalize, tokenize, count_freq, top_n

def main():
    text = input()
    norm = normalize(text)
    words = tokenize(norm)
    freq = count_freq(words)
    top = top_n(freq, 5)
    tokens = len(words)
    unique = len(freq.items())
        
    print(f"Всего слов: {tokens}")
    print(f"Уникальных слов: {unique}")
    print("Топ-5:")
    for word, count in top:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
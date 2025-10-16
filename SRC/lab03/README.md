# Лабораторная работа 3

### задание A

``` python
import re
from collections import Counter

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if type(text) is not str:
        raise TypeError
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = re.sub(r'[\t\r\n\f\v]', ' ', text)
    return re.sub(r' +', ' ', text).strip()

def tokenize(text: str) -> list[str]:
    if type(text) is not str:
        raise TypeError
    return re.findall(r'\b[\w]+(?:-[\w]+)*\b', text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    if type(tokens) is not list:
        raise TypeError
    return dict(Counter(tokens))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if type(freq) is not dict:
        raise TypeError
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]
```
![img1](/images/lab3/ex3A.png)

### задание B

``` python
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
```
![img2](/images/lab3/ex3B.png)


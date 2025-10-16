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
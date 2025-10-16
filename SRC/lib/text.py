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

print('normilize')
print(r'ПрИвЕт\nМИр\t  Out: ', normalize('ПрИвЕт\nМИр\t'))
print(r'ёжик, Ёлка  Out: ', normalize('ёжик, Ёлка', yo2e = True))
print(r'Hello\r\nWorld  Out: ', normalize('Hello\r\nWorld'))
print(r' двойные пробелы   Out: ', normalize(' двойные пробелы '))

print('tokenize')
print(r'привет мир Out:', tokenize('привет мир'))
print(r'hello,world!!! Out:', tokenize('hello,world!!!'))
print(r'по-настоящему круто Out:', tokenize('по-настоящему круто'))
print(r'2025 год Out:', tokenize('2025 год'))
print(r'emoji 😀 не слово Out:', tokenize('emoji 😀 не слово'))

print('count_freq & top_n')
freq1 = count_freq(["a","b","a","c","b","a"])
print(f'["a","b","a","c","b","a"], --> {freq1}, --> {top_n(freq1, 2)}')

freq2 = count_freq(["bb","aa","bb","aa","cc"])
print(f'["bb","aa","bb","aa","cc"], --> {freq2}, --> {top_n(freq2, 2)}')
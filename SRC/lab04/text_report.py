import sys
import argparse
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from io_txt_csv import read_text, write_csv
from text import *

def parse_args():
    parser = argparse.ArgumentParser(
        description='Анализ частоты слов в тексте и генерация CSV отчета',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python src/lab04/text_report.py
  python src/lab04/text_report.py --in data/input.txt --out data/report.csv
  python src/lab04/text_report.py --encoding cp1251
        """
    )
    parser.add_argument('--in', dest='input_file', default='data/lab04/input.txt',
                       help='Входной файл (по умолчанию: data/lab04/input.txt)')
    parser.add_argument('--out', dest='output_file', default='data/lab04/report.csv',
                       help='Выходной CSV файл (по умолчанию: data/lab04/report.csv)')
    parser.add_argument('--encoding', default='utf-8',
                       help='Кодировка входного файла (по умолчанию: utf-8)')
    
    return parser.parse_args()

def print_summary(word_counts: dict, top_n_count: int = 5):
    total_words = sum(word_counts.values())
    unique_words = len(word_counts)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    
    if unique_words > 0:
        top_words = top_n(word_counts, top_n_count)
        print("Топ-5:")
        for word, count in top_words:
            print(f"{word}:{count}")
    else:
        print("Топ-5: нет слов")

def main():
    args = parse_args()
    
    try:
        text = read_text(args.input_file, args.encoding)
        normalized_text = normalize(text)
        tokens = tokenize(normalized_text)
        word_counts = count_freq(tokens)
        sorted_words = top_n(word_counts, len(word_counts))
        
        header = ('word', 'count')
        write_csv(sorted_words, args.output_file, header)
        print_summary(word_counts)
                
    except FileNotFoundError:
        print(f"Ошибка: Файл '{args.input_file}' не найден")
        print("Проверьте путь к файлу и его существование")
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"Ошибка кодировки: {e}")
        print("Попробуйте указать правильную кодировку через --encoding")
        print("Например: --encoding cp1251 для Windows-1251")
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
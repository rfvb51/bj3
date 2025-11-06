# Лабораторная работа 5

### задание A

``` python
import csv
from pathlib import Path

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX используя openpyxl.
    """
    # Проверка существования файла
    if not Path(csv_path).exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")
    
    # Проверка расширения файла
    if not csv_path.lower().endswith('.csv'):
        raise ValueError("Неверный тип файла. Ожидается .csv")
    
    if not xlsx_path.lower().endswith('.xlsx'):
        raise ValueError("Неверный тип файла. Ожидается .xlsx")
    
    try:
        from openpyxl import Workbook
        from openpyxl.utils import get_column_letter
        
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"
        
        # Читаем CSV
        with open(csv_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)
        
        # Проверки
        if not data:
            raise ValueError("Пустой CSV файл")
        
        if not data[0]:
            raise ValueError("CSV файл не содержит заголовка")
        
        # Записываем данные
        for row in data:
            ws.append(row)
        
        # Настройка ширины колонок
        for i, column_cells in enumerate(ws.columns, 1):
            length = 8  # минимальная ширина
            for cell in column_cells:
                if cell.value:
                    length = max(length, len(str(cell.value)))
            ws.column_dimensions[get_column_letter(i)].width = length + 2
        
        wb.save(xlsx_path)
    
    except ImportError:
        raise ImportError("Для работы функции требуется установить openpyxl: pip install openpyxl")
    except Exception as e:
        raise ValueError(f"Ошибка конвертации: {e}")

csv_to_xlsx('data/samples/cities.csv', 'data/out/output.xlsx')
```
![img1](/images/lab5/ex5A.s.j.png)

![img2](/images/lab5/ex5A.o.c.png)

![img3](/images/lab5/ex5A.s.c.png)

![img4](/images/lab5/ex5A.o.j.png)

### задание B

``` python
import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    # Проверка существования файла
    if not Path(json_path).exists():
        raise FileNotFoundError(f"Файл {json_path} не найден")
    
    # Проверка расширения файла
    if not json_path.lower().endswith('.json'):
        raise ValueError("Неверный тип файла. Ожидается .json")
    
    try:
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except json.JSONDecodeError:
        raise ValueError("Ошибка декодирования JSON")
    
    # Проверка структуры данных
    if not isinstance(data, list):
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    if len(data) == 0:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    # Проверка что все элементы - словари
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Список содержит не-словари")
    
    # Получаем все возможные поля из всех словарей
    all_fields = set()
    for item in data:
        all_fields.update(item.keys())
    
    # Сортируем поля по алфавиту (как указано в README)
    fieldnames = sorted(all_fields)
    
    try:
        with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in data:
                # Заполняем отсутствующие поля пустыми строками
                complete_row = {field: row.get(field, '') for field in fieldnames}
                writer.writerow(complete_row)
                
    except Exception as e:
        raise ValueError(f"Ошибка записи CSV: {e}")

json_to_csv('data/samples/people.json', 'data/out/output.csv')

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    # Проверка существования файла
    if not Path(csv_path).exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")
    
    # Проверка расширения файла
    if not csv_path.lower().endswith('.csv'):
        raise ValueError("Неверный тип файла. Ожидается .csv")
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            
            # Проверка наличия заголовка
            if reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовка")
            
            data = list(reader)
            
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    
    # Проверка что файл не пустой
    if len(data) == 0:
        raise ValueError("Пустой CSV файл")
    
    try:
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)
            
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")
    
csv_to_json('data/samples/people.csv', 'data/out/output.json')
```
![img5](/images/lab5/ex5B.png)
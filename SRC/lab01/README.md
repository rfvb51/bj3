# 4951

## Лабораторная работа 1

### задание 1

``` python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
![img1](/images/lab1/ex1.png)

### задание 2

``` python
a_input = input("Число a: ").replace(',', '.')
b_input = input("Число b: ").replace(',', '.')

a = float(a_input)
b = float(b_input)

sum_ab = a + b
avg_ab = sum_ab / 2

print(f"sum = {sum_ab:.2f}; avg = {avg_ab:.2f}")
```
![img2](/images/lab1/ex2.png)

### задание 3

``` python
price = float(input("price: ").replace(',', '.'))
discount = float(input("discount: ").replace(',', '.'))
vat = float(input("vat: ").replace(',', '.'))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} ₽")
print(f"НДС:               {vat_amount:.2f} ₽")
print(f"Итого к оплате:    {total:.2f} ₽")
```
![img3](/images/lab1/ex3.png)

### задание 4

``` python
m = int(input("Минуты: "))

hours = m // 60
minutes = m % 60

print(f"{hours}:{minutes:02d}")
```
![img4](/images/lab1/ex4.png)

### задание 5

``` python
fullname = input("ФИО: ")
newname = ' '.join(fullname.split())

words = newname.split()
initials = ''.join(word[0].upper() for word in words)

print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(newname)}")
```
![img5](/images/lab1/ex5.png)
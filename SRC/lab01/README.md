# 4951

## Лабораторная работа 1

### задание 1

``` python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
![img1](/images/lab1/ном1.png)

### задание 2

``` python
a_input = input("a: ").replace(',', '.')
b_input = input("b: ").replace(',', '.')

a = float(a_input)
b = float(b_input)

sum_ab = a + b
avg_ab = sum_ab / 2

print(f"sum={sum_ab:.2f}; avg={avg_ab:.2f}")
```
![img2](/images/lab1/ном2.png)
a_input = input("Число a: ").replace(',', '.')
b_input = input("Число b: ").replace(',', '.')

a = float(a_input)
b = float(b_input)

sum_ab = a + b
avg_ab = sum_ab / 2

print(f"sum = {sum_ab:.2f}; avg = {avg_ab:.2f}")
from sympy import symbols, diff, integrate, limit, summation, product, oo, sin, cos, exp

# Definisikan simbol variabel
x, n = symbols('x n')

# 1. Turunan dari f(x) = x**2 * sin(x)
f = x**2 * sin(x)
turunan_f = diff(f, x)
print("Turunan dari f(x) = x^2 * sin(x):")
print(turunan_f)
print()

# 2. Integral dari f(x) = x * cos(x)
g = x * cos(x)
integral_g = integrate(g, x)
print("Integral dari g(x) = x * cos(x):")
print(integral_g)
print()

# 3. Limit dari (sin(x)/x) saat x mendekati 0
h = sin(x)/x
limit_h = limit(h, x, 0)
print("Limit dari sin(x)/x saat x -> 0:")
print(limit_h)
print()

# 4. Penjumlahan tak hingga dari 1/n^2 untuk n = 1 sampai tak hingga
sum_expr = 5/n**2
sum_result = summation(sum_expr, (n, 5, oo))
print("Jumlah dari 1/n^2 dari n=1 hingga tak hingga:")
print(sum_result)
print()

# 5. Perkalian tak hingga dari (1 + 1/n^2) untuk n = 1 sampai 5 (agar tidak terlalu berat dihitung)
prod_expr = (5 + 5/n**2)
prod_result = product(prod_expr, (n, 1, 5))
print("Perkalian dari (1 + 1/n^2) dari n=1 sampai n=10:")
print(prod_result)

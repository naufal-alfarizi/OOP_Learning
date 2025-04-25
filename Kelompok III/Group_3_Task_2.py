from sympy import symbols, Rational, Float, Integer, simplify, expand, evalf

# 1. Jenis number
a = Integer(10)             # Bilangan bulat
b = Rational(3, 4)         # Bilangan rasional
c = Float(3.1415)          # Bilangan float

print("Jenis Number:")
print("Integer a:", a, type(a))
print("Rational b:", b, type(b))
print("Float c:", c, type(c))
print()

# 2. Ekspresi simbolik
x, y = symbols('x y')
expr = (x + y)**2

print("Ekspresi simbolik:")
print("Ekspresi: (x + y)^3 =", expr)
print()

# 3. Ekspansi dan penyederhanaan ekspresi
expanded_expr = expand(expr)
simplified_expr = simplify(expanded_expr)

print("Ekspresi setelah di-expand:")
print(expanded_expr)
print("Penyederhanaan dari ekspresi:")
print(simplified_expr)
print()

# 4. Evaluasi numerik
numeric_expr = (Rational(1, 3) + Rational(2, 10))
print("Evaluasi numerik dari 1/3 + 2/10:")
print("Hasil simbolik:", numeric_expr)
print("Hasil desimal:", numeric_expr.evalf())

import sympy as sp
from sympy import symbols, diff, integrate, limit, sin, cos, exp, log, oo, Sum, Product, pi, factorial, pprint

def main():
    print("=== OPERASI KALKULUS ===")
    x, y, n, k = symbols('x y n k')
    
    # 1. Turunan (Derivatif)
    print("\n1. TURUNAN (DERIVATIF)")
    expr1 = 3*x**4 - 2*x**3 + 5*x - 7
    deriv1 = diff(expr1, x)
    print(f"Turunan dari {expr1} terhadap x: {deriv1}")
    
    expr2 = sin(x)*cos(x)
    deriv2 = diff(expr2, x)
    print(f"Turunan dari {expr2} terhadap x: {deriv2}")
    
    # Turunan parsial
    expr3 = x**2 * y + sin(x * y)
    deriv3_x = diff(expr3, x)
    deriv3_y = diff(expr3, y)
    print(f"\nTurunan parsial dari {expr3}:")
    print(f"terhadap x: {deriv3_x}")
    print(f"terhadap y: {deriv3_y}")
    
    # 2. Integral
    print("\n2. INTEGRAL")
    # Integral tak tentu
    int_expr1 = integrate(x**2 + 3*x - 2, x)
    print(f"Integral tak tentu dari x^2 + 3x - 2: {int_expr1}")
    
    # Integral tentu
    int_expr2 = integrate(sin(x), (x, 0, pi))
    print(f"\nIntegral tentu dari sin(x) dari 0 sampai pi: {int_expr2}")
    
    # Integral ganda
    int_expr3 = integrate(x*y, (x, 0, 1), (y, 0, 2))
    print(f"\nIntegral ganda dari x*y dx(0-1) dy(0-2): {int_expr3}")
    
    # 3. Limit
    print("\n3. LIMIT")
    # Limit biasa
    lim_expr1 = limit((sin(x)/x),x,0)
    print(f"Limit sin(x)/x saat x mendekati 0: {lim_expr1}")
    
    # Limit tak hingga
    lim_expr2 = limit((1 + 1/x)**x, x, oo)
    print(f"\nLimit (1 + 1/x)^x saat x mendekati tak hingga: {lim_expr2}")
    
    # 4. Sum (Penjumlahan)
    print("\n4. SUM (PENJUMLAHAN)")
    # Sum sederhana
    sum1 = Sum(k, (k, 1, 5))
    print(f"\na) Sum dari k=1 sampai 5:")
    pprint(sum1)
    print("Hasil:", sum1.doit())
    
    # Sum dengan ekspresi matematika
    sum2 = Sum(k**2, (k, 1, n))
    print(f"\nb) Sum dari k^2 dari k=1 sampai n:")
    pprint(sum2)
    print("Rumus umum:", sum2.doit())
    
    # Sum tak hingga (konvergen)
    sum3 = Sum(1/k**2, (k, 1, oo))
    print(f"\nc) Sum tak hingga 1/k^2:")
    pprint(sum3)
    print("Hasil:", sum3.doit())
    
    # 5. Product (Perkalian)
    print("\n5. PRODUCT (PERKALIAN)")
    # Product sederhana (faktorial)
    prod1 = Product(k, (k, 1, 5))
    print(f"\na) Product dari k=1 sampai 5 (5!):")
    pprint(prod1)
    print("Hasil:", prod1.doit())
    
    # Product dengan ekspresi matematika
    prod2 = Product(1 + 1/k, (k, 1, n))
    print(f"\nb) Product dari (1 + 1/k) dari k=1 sampai n:")
    pprint(prod2)
    print("Hasil:", prod2.doit())
    
    # Product tak hingga (konvergen)
    prod3 = Product(exp(1/k**2), (k, 1, oo))
    print(f"\nc) Product tak hingga e^(1/k^2):")
    pprint(prod3)
    print("Hasil:", prod3.doit().simplify())

if __name__ == "__main__" :
    main()
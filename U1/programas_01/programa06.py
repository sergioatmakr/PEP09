# Operadores en Python usando estilo printf

# ----------------------------
# Operadores aritméticos
# ----------------------------
a = 10
b = 3

print("OPERADORES ARITMÉTICOS")
print("%d + %d = %d" % (a, b, a + b))
print("%d - %d = %d" % (a, b, a - b))
print("%d * %d = %d" % (a, b, a * b))
print("%d / %d = %.2f" % (a, b, a / b))   # división flotante con 2 decimales
print("%d // %d = %d" % (a, b, a // b))
print("%d %% %d = %d" % (a, b, a % b))     # para imprimir el símbolo % se usa %%
print("%d ** %d = %d" % (a, b, a ** b))
print()

# ----------------------------
# Operadores lógicos
# ----------------------------
x = True
y = False

print("OPERADORES LÓGICOS")
print("%s and %s = %s" % (x, y, x and y))
print("%s or %s = %s" % (x, y, x or y))
print("not %s = %s" % (x, not x))
print("not %s = %s" % (y, not y))
print()

# ----------------------------
# Operadores de comparación
# ----------------------------
print("OPERADORES DE COMPARACIÓN")
print("%d == %d -> %s" % (a, b, a == b))
print("%d != %d -> %s" % (a, b, a != b))
print("%d > %d -> %s" % (a, b, a > b))
print("%d < %d -> %s" % (a, b, a < b))
print("%d >= %d -> %s" % (a, b, a >= b))
print("%d <= %d -> %s" % (a, b, a <= b))
print("%s == %s -> %s" % (x, y, x == y))
print("%s != %s -> %s" % (x, y, x != y))
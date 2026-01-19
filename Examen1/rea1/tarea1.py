minutos=int(input("Introduce una cantidad de minutos: "))

horas=int(minutos/60)
resto=minutos-horas*60

print(f"Equivale a {horas} horas y {resto} minutos")
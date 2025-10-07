dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
anio = int(input("Introduce el año: "))

fecha_valida = True

if mes < 1 or mes > 12:
     fecha_valida = False
else:
        
    if mes in [1, 3, 5, 7, 8, 10, 12]:
         dias_max = 31
    elif mes in [4, 6, 9, 11]:
         dias_max = 30
    elif mes == 2:
        if (anio%4==0 and anio%100!=0)or anio%400==0:
            dias_max = 29
        else:
            dias_max = 28

    if dia < 1 or dia > dias_max:
        fecha_valida = False

if fecha_valida:
    print(f"La fecha {dia}/{mes}/{anio} es válida.")
else:
    print(f"La fecha {dia}/{mes}/{anio} NO es válida.")

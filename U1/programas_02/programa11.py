
HH = int(input("Hora de salida (HH): "))
MM = int(input("Minutos de salida (MM): "))
SS = int(input("Segundos de salida (SS): "))
N = int(input("Tiempo de viaje en segundos (N): "))


salida_segundos = HH * 3600 + MM * 60 + SS

llegada_segundos = salida_segundos + N

HH_llegada = (llegada_segundos // 3600) % 24
MM_llegada = (llegada_segundos % 3600) // 60
SS_llegada = llegada_segundos % 60

print(f"Hora de llegada: {HH_llegada:02d}:{MM_llegada:02d}:{SS_llegada:02d}")
bytes_total = int(input("Introduce el número de bytes: "))

KB_dec = bytes_total / 10**3
MB_dec = bytes_total / 10**6
GB_dec = bytes_total / 10**9

KiB_bin = bytes_total / 1024
MiB_bin = bytes_total / (1024**2)
GiB_bin = bytes_total / (1024**3)

print("\n--- Sistema Decimal (Base 10) ---")
print(f"{GB_dec:.2f} GB")
print(f"{MB_dec:.2f} MB")
print(f"{KB_dec:.2f} KB")
print(f"{bytes_total} Bytes")

print("\n--- Sistema Binario (Base 2) ---")
print(f"{GiB_bin:.2f} GiB")
print(f"{MiB_bin:.2f} MiB")
print(f"{KiB_bin:.2f} KiB")
print(f"{bytes_total} Bytes")

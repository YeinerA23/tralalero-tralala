tabla = int(input("que tabla de multiplicar quieres ver?: "))
print(f"tabla de multiplicar del {tabla}:")
for h in range(1, 11):
    print(f"{tabla} x {h} = {tabla * h}")
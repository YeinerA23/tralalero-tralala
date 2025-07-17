num1 = int(input("agregue primer numero: "))
num2 = int(input("agregue segundo numero mayor al primero: "))
if num1 < num2:
    numero = list(range(num1 + 1, num2))
else:
    numero = list(range(num1 - 1, num2 - 1))

print(f"los numeros entre {num1} y {num2} son {numero}")
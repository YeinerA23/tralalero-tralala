import cmath
a = float(input("ingese e valor de a: "))
b = float(input("ingese e valor de b: "))
c = float(input("ingese e valor de c: "))
x = (-b- cmath.sqrt(b**2-4*a*c))/(2*a)
x2 = (-b+ cmath.sqrt(b**2-4*a*c))/(2*a)
print (x)
print(x2)

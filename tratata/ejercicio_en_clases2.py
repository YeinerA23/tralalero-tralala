
usuario = input("Ingrese su nombre de usuario: ")

while usuario != "yeiner":
    print("Usuario no es correcto")
    usuario = input("Intente nuevamente: ")

print("Usuario correcto")


contraseña = input("Ingrese contraseña: ")

while contraseña != "pepito123":
    if len(contraseña) <= 9:
        print("Su contraseña es suficientemente larga")

        if contraseña == "pepito123":
            print("Contraseña correcta")
        else:
            print("Contraseña incorrecta")
    else:
        print("Caracteres insuficientes")

    contraseña = input("Intente nuevamente: ")

print("Acceso concedido")
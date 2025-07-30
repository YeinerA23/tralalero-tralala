continuar = "S"
while continuar != "N":
    
    sueldo = float(input("ingrese su sueldo: "))
    aumento1 = sueldo * 0.06
    total1 = sueldo + aumento1
    print(f"su sueldo con el aumento del 6% quedara en {aumento1 + sueldo}")

    if total1 <= 380000:
        aumento2 = total1 * 0.10
        total2 = total1 + aumento2
        print(f"has sido beneficiario a un segundo auemento del 10% y te quedara en {total2}")
        
    else:
        print("usted no sera beneficiario del segundo aumento")
        
    continuar = str(input("precione S para continaur y N par detenerce: "))
        
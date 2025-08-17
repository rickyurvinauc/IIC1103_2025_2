# pedir edad
edad = int(input("Ingresa tu edad: "))

# verificar rango de edad
if edad < 12:
    print("El precio es 5")
elif edad >= 12 and edad <= 17:
    print("El precio es 8")
else:
    # aqui ya sabemos que tiene 18 o mas
    estudiante = input("Eres estudiante? (si/no): ")
    if estudiante == "si":
        print("El precio es 7")
    else:
        print("El precio es 10")
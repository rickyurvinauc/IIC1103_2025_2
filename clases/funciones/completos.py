def hacer_completo():
    print("Abrir pan")
    print("Poner mayonesa")
    print("Agregar palta, tomate y mayo")
    print("Servir completo italiano")

hacer_completo()


def hacer_completo(tipo):
    print("Abrir pan")
    print("Poner mayonesa")
    
    if tipo == "italiano":
        print("Agregar palta, tomate y mayo")
    elif tipo == "dinámico":
        print("Agregar americana, mayo y kétchup")
    else:
        print("Agregar solo vienesa")
    
    print(f"Servir completo {tipo}")

hacer_completo("italiano")
hacer_completo("dinámico")

def precio_completo(tipo):
    if tipo == "italiano":
        return 2000
    elif tipo == "dinámico":
        return 1800
    else:
        return 1500

total = precio_completo("italiano") * 3
print("Total a pagar:", total)
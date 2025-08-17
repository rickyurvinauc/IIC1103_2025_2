# pedir dos numeros al usuario
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

# operaciones basicas
print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicacion:", num1 * num2)

# verificar division por cero
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("No se puede dividir por cero")
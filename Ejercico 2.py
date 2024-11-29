# Actividad 1
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
print("-------------------------------------------------------")


# Actividad 2
valor = int(input("Ingresa un número: "))

if valor > 20:
    print(f"El número {valor} es mayor que 20.")
elif valor < 20:
    print(f"El número {valor} es menor que 20.")
else:
    print(f"El número {valor} es igual a 20.")



print("-------------------------------------------------------")


# Actividad 3
edad = int(input("Ingresa tu edad: "))

if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad <= 65:
    print("Eres un adulto.")
else:
    print("Eres una persona mayor.")



print("-------------------------------------------------------")

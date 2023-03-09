#Estructuras Repetitivas

#Estructura "while": permite ejecutar
# un bloque de código mientras se cumple una condición específica.

print("inicializando sentencia while")
numero1= int(input("ingresa un numero: "))
while numero1 >= 0:
    print(numero1)
    numero1 -= 1
print("finalizando sentencia while")
print("#################################################################")

#Estructura "for": permite ejecutar un bloque de código
# para cada elemento en una secuencia (como una lista o una cadena de caracteres).

print("inicializando sentencia for")
numeros = [2, 5, 8, 3, 15, 20,76,45]
limite = 8
contador = 0

for numero in numeros:
    if numero > limite:
        contador += 1

print("El número de elementos en la lista que son mayores que", limite, "es:", contador)
print("Fin del programa")

print("finalizando sentencia for")
print("#################################################################")

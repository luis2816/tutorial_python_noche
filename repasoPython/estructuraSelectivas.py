#Estructuras selectivas

#Estructura "if": permite ejecutar un bloque de código si se
# cumple una condición específica. También puede incluir una
# cláusula "else" para ejecutar un bloque de código alternativo
# si la condición no se cumple.

print("iniciando sentencia if/else")
numero1= int(input("Ingresa un numero: "))
if numero1 < 18:
    print(numero1, "es menor que 18")
else:
    print(numero1, " es mayor que 18")
print("finalizando sentencia if/else")
print("#################################################################")

#Estructura "if-elif-else": permite ejecutar diferentes bloques de código
# en función de varias condiciones. La cláusula "elif" se utiliza para evaluar
# una condición adicional si la condición anterior no se cumple.

print("iniciando sentencia if-elif-else")
nombre= str(input("Ingresa tu nombre: "))
edad= int(input("ingresa tu edad: "))

if edad < 18:
    print(nombre, "Eres menor de edad")
elif edad < 25:
    print(nombre, "Eres mayor de edad pero todavía joven")
elif edad < 40:
    print(nombre, "Eres adulto joven")
else:
    print(nombre, "Eres adulto mayor")

print("finalizando  sentencia if-elif-else")
print("#################################################################")

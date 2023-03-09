# Tuplas

# Crear Tupla
print("Creamos una tupla")
tupla = (1, 2, 3, 4, 5)
tupla2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("Imprimimos nuestra Tupla1 = ", tupla, "y nustra tupla2 = ", tupla2)
print("#################################################################")

# Acceder a elementos de una tupla
print("Acediendo a elemntos de una tupla")
print("Imprimiedo el valor de la tupla en la poción 2 = ", tupla[2])
print("#################################################################")

#Desempacar una tupla
print("Desempaquetando mi tupla")
a, b, c, d, e = tupla
print("imprimiendo a = ", a, "imprimiendo b = ", b, "imprimiendo c = ", c, "imprimiendo d = ", d, "imprimiendo e = ", e )
print("#################################################################")


#  Utilizar tuplas como elementos de una lista
print("utilizando mi tupla como elemtos de una lista")
mi_lista=[tupla, tupla]
print("imprimiendo mi lista utilizando mi tupla = " , mi_lista)
print("#################################################################")

#comparar tuplas
print("comparamos nuestras dos tuplas")
if tupla < tupla2:
    print("tupla1 es menor que tupla2")
else:
    print("tupla2 es menor que tupla1")


print("#################################################################")
#Utilizar tuplas como claves en un diccionario:
print("utilizando mis tuplas como vlaves en un diccionario")
mi_diccionario = {tupla: "valor1", tupla2: "valor2"}
print(mi_diccionario[(1, 2, 3, 4, 5)]) # imprime "valor1"
print("#################################################################")


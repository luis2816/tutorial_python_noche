#Listas estándar: Es la lista más común en Python
# y puede contener cualquier tipo de datos, incluyendo
# otras listas. Se definen utilizando corchetes [ ] y
# los elementos se separan por comas.

mi_lista = [1, 2,4.5, "hola", False, [3, 4, 5]]
print("Listas estandar" , mi_lista)
print("finalizando listas estandar")
print("#################################################################")

#Listas anidadas: Son listas que contienen otras listas como elementos.
print("Inicializando listas anidadas")
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("listas anidadas: ", lista_anidada)
print("finalizando listas anidadas")
print("#################################################################")
#Listas vacías: Son listas que no contienen elementos.
# Se definen utilizando corchetes vacíos [ ] o utilizando la función list().
print("Inicializando listas vaccias")
lista_vacia = []
lista_vacia2 = list()

print("lista vacia" , lista_vacia)
print("lista vacia utilizando la función list() = ", lista_vacia2)
print("finalizando listas vaccias")
print("#################################################################")

#Listas de rango: Son listas que contienen
# una secuencia de números que se pueden generar utilizando la función range().
print("Inicializando listas de rango")
lista_rango = list(range(20))
print("lista de rango = " , lista_rango)
print("Finalizando listas de rango")
print("#################################################################")

#Listas ordenadas: Son listas que mantienen un orden específico
# para sus elementos. Se pueden definir utilizando la función sorted().
print("Inicializando listas ordenadas")
lista_desordenada = [3, 1, 4, 2, 5, 6, 9, 23, 20, 17]
lista_ordenada = sorted(lista_desordenada)
print("lista desornedada =" , lista_desordenada)
print("lista ordenada =" , lista_ordenada)
print("Finalizando listas ordenadas")
print("#################################################################")

#Listas de comprensión: Son listas que se pueden construir de manera más compacta
# utilizando una sintaxis especial. Permiten crear una nueva lista a partir de otra lista o secuencia.
print("Inicializando lista de comprensiones")
mi_lista = [1, 2, 3, 4, 5]
nueva_lista = [num * 3 for num in mi_lista]
print(nueva_lista)
print("Finalizando lista de comprensiones")

print("#################################################################")





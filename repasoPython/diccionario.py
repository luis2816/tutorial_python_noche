# Crear un dicionario
print("Creamos un diccionario")
diccionario = {"nombre": "felipe", "apellido": "ordoñez", "edad": "22"}
print("imprimimos nuestro diccionario =", diccionario)
print("#################################################################")

#Acceder a valores en un diccionario utilizando claves
print("accediendo a los valores del dicionario utilizando sus claves")
print("accediendo al valor con la clave nombre= ", diccionario["nombre"])
print("accediendo al valor con la clave apellido= ", diccionario["apellido"])
print("#################################################################")

#Agregar o actualizar valores en un diccionario
print("agregando y actualizando valores en mi diccionario")
diccionario["trabajo"] = "programador"
diccionario["edad"] = 20
print("imprimiendo el dicionario con los cambios = ", diccionario)
print("#################################################################")

#Eliminar elemtos de un dicionario
print("eliminando elemtos de eun dicionario")
del diccionario["trabajo"]
print("imprimimos el dicionario con el elemento ya eliminado= " , diccionario)
print("#################################################################")


#Verificar si una clave existe en un diccionario:
print("verificando si la  clave edad existe en el dicionario")
if "edad" in diccionario:
    print("La clave 'edad' existe en el diccionario")
else:
    print("La clave 'edad' no existe en el diccionario")
print("#################################################################")


#iterar atravez de un diccionario
print("iterando nuestro diccionario")
for clave, valor in diccionario.items():
    print(clave + ":", valor)
print("#################################################################")

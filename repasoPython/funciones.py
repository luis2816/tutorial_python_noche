# Funciones
def miFuncion():
    print("Hola Mundo")


miFuncion()

def mostrarNombre(nombre, apellido):
    print("su nombre es: "+ nombre + " " + apellido)


mostrarNombre("Felipe", "Diaz") # Invocar la función


# Entrada
base= float(input("ingrese la base: "))
altura= float(input("ingrese la altura"))

#proceso
def calcularAreaTriangulo(b,a):
    area= (b*a)/2
    return  area
#salida
resultado= calcularAreaTriangulo(base, altura)
print("El area del triangulo es: ", resultado)

def mostrarMensaje(pais="colombia"):
    print("yo soy de : "+pais)
mostrarMensaje("Suiza")
mostrarMensaje("Ecuador")
mostrarMensaje()
mostrarMensaje("Argentina")
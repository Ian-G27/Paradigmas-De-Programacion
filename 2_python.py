#=========================================
#    Ian Diego Buendia Alvarez 
#=========================================
#    Matematica algoritmica
#    ESFM IPN
#    Septiembre de 2023
#========================================

#========================================
#  Input permite obtener datos del usuario promter
#========================================
nombre = input("Dame tu nombre: ")
print("Hola como estas",nombre)

#========================================
# Los enteros son de presicion ilimitada
#========================================
y = 500000000000000000000
print(y)

#==========================================
# La funcion int() cambia strings y floats a enteros
#==========================================
numero = int(input("Dame tu edad: "))
type(numero)

#==========================================
# La notacion cientifica de flotantes  utiliza e o E
#===========================================
# 1.2 x 10^{-9}
#===========================================
y = float("14.3")
print(y)

#=========================================================
# Los complejos se escriben con la raiz de menos uno
# j siempre con su numero como prefijo 
# no acepta la j suelta
#=========================================================
z = 1+1j

# suma +
# resta -
# multiplicacion *
# division /
# modulo %
# exponente **
# // funcion piso
# Funciones para transformar numeros int() float() complex()
# Operaciones abs() round() pow()

print(round(3.14159,4))

#=========================
# Strings de varias lineas 
#===========================
parrafo = """ En el bosque de la china 
 la chinita se perdio """
print(parrafo)
#================================
n=len(parrafo)
print(n)

#=========================================================
# Las letras en un string ocupan lugares como un arreglo 
#  (tambien de atras adelante comenzando en -1 el ultimo)
#==========================================================
palabra = "hola"
print(palabra[0])
print(palabra[-4])

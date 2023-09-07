#=================================
#     Ian Diego Buendia Alvarez
#=================================
# Paradigmas de programacion
# Matematica Algoritmica
#      ESFM-IPN   7-sept3-2023
#=================================

'''ESTE ERS UN SUPERCOMENTARIO DE 
   DE INICIO A NUESTRO RESUMEN
'''
#============================
# Operaciones basicas
#============================
print (2+3)
print (2*3)
print (2/3)
print (2**10)
print (2**0.5)   #Para la raiz cuadrada
print (10%2)
print (10%0.1)    #Esclusivo en python
#====================================
# Para saber el tipo de objeto se usa type
#====================================
t=0
print (type(t)) #entero
t=3.6
print(type(t)) # real (flotante)
t=True
print(type(t)) #booleano (bool)

#=============================
# Mensajes a pantalla
#=============================
print("Este es un comando de python. " , "Este es otro enunciado.", t)
print('id: ', 1)
print('first Name: ', 'IAN')
print('Last Name: ', 'DIEGO')
print ("vamos a sumar esto" + "con esto otro")

#=====================================
# Continuar una instruccion en varios renglones
#===============================================
if 100>99 and \
        200 <= 300 and \
        True != False:
            print('Hello wordl!')

#====================================================
# Comandos diferentes en la misma linea
#====================================================
print("Hola "); print("tu!!")  #SE considera mala practica

#======================================================
# usando parenrtesis redondondos
#==================================================
list = [1 , 2, 3, 4,
        5, 6, 7, 8, 
        9, 10, 11, 12,]
matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(list)
print(matriz)

#========================================================
# Indentacion estricta para procesos dependientes de: (dos puntos)
#===========================================================
if 10>5:
    print ("diez es mayor que cinco")
    print("otra identacion")
    for i in list:
        print (i)
        print("ok")
if 10>5:
    print("verdadero")
    if 10<20:
        print ("verdadera")
elif 5>3: # comienza segundo condicional
    print("esto no se imprimira")
else: 
    print ("aqui nunca llega")

#=====================
# Funciones
#=====================
def say_hello(name):
    print("Hello",name)
    print("welcome to python Tutorials")

say_hello("Ian")


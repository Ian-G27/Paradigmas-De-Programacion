#==========================================
#   Ian Diego Buendia Alvarez
#==========================================
#  Matematica Algoritmica 
#  Paradigmas de Programacion
#  ESFN IPN octubre 2023
#==========================================

#=================================================
#  La clase ClienteBancario esta el subdirectorio
#  aplicacion/banco/
#==================================================
from aplicacion.banco.cliente_bancario import ClienteBancario 

#==================================================
# try: intenta (correr las instrucciones)
# except: atrapar el error en una variable
#  e se puede convertir a string
#==================================================

#==================================================
# Error por sacar mas dinero del que tiene
#==================================================
try:
    cliente = ClienteBancario("Jaime Andrade", "Hernandez Sanchez", 28, 0,0)
    cliente.guardarDinero(300)
    print(cliente.imprimirInfo())
    cliente.retirarDinero(400)
    print(cliente.imprimirInfo())
#==============================================
#  Exception es el objeto mas general de error
#==============================================
except Exception as e:
    print("Error: " + str(e))

#================================================
# Error por usar un atributo privado
#===============================================
try: 
    print(cliente.__nombres)
except Exception as ex:
    print("Error: " + str(ex))

#=================================================
#  Forma correcta
#=================================================
print(cliente.nombres)

#=========================================
#  Clase ClienteBancario
#=========================================
class ClienteBancario: 
    __nombres:str = None
    __apellidos:str = None
    __edad:int = 0
    __balanceDeCuenta:float == 0.0

    def __init__(self, nombres:str, apellidos:str, edad:int=0, balanceDeCuenta: float=0.0):
        self.__validarEdad(edad)
        self.__validarCantidad(balanceDeCuenta)
        self.nombres = nombres
        self.apellidos = apellidos
        self.__edad = edad
        self.balanceDeCuenta = balanceDeCuenta
    def getNombreCompleto(self) -> str:
        return self.nombres + " "+ self.apellidos

    def __mandarEmail(self, titulo:str, texto:str) -> None:
        print("mandar email: " + titulo + " con texto: " + texto)

    def __enviarBalanceAlBanco(self, cantidad:float) -> None:
        print("Enviando cantidad: " + str(cantidad) + " al banco...")

    #================================================
    #  Metodo privado con dos guones bajos
    #  Si la edad es menhor que 18 genera un error
    #================================================
    def __validarEdad(self, edad:int) -> None: 
        if edad < 18:
           raise Exception("Es menor de edad")
        
    def imprimirInfo(self) -> str:
        return "Nombre: " + self.getNombreCompleto() + " , Edad: " + str(self.edad) + " , Balance: "+ str(self.__balanceDeCuenta)
    
    #==============================================================
    #  Metodo privado que checa si el balance es negativo
    #  y genera un error
    #==============================================================
    def __validarCantidad(self, balanceDeCuenta:float) -> None:
        if balanceDeCuenta < 0:
            raise Exception("El balance en la cuenta no puede ser negativo")
        
    def guardarDinero(self, cantidad:float) -> None:
       self.__balanceDeCuenta = self.__balanceDecuenta + cantidad
       self.__mandarEmail("---- guardando deposito ----", "se recibieron " + str(cantidad))
       self.___enviarBalanceAlBanco(cantidad)

    def retirarDinero(self, cantidad: float) -> None:
        cantidadFinal = self.__balanceDeCuenta - cantidad
        self.__validarCantidad(cantidadFinal)
        self.__balanceDeCuenta = cantidadFinal
        self.__mandarEmail("--- retirando dinero----", " se retiro "+ str(cantidad))
        self.__enviarBalanceAlBanco(cantidad)
        

    
    

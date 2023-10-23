#=============================================
#   Ian Diego Buendia Alvarez
#=============================================
#    Matematica algoritmica
#    Paradigmas de programacion
#  ESFM-IPN
#=============================================

#=============================================
#   Conjunto en python
#=============================================
even_nums = {2 , 4, 6, 8, 10}     # Conjunto de numeros
print(even_nums)

#  El bool no es parte de un conjunto 
emp = {1, 'Steve',10.5, True}  # conjunto de diferentes objetos
print(emp)

nums = {1, 2, 2, 3, 4, 4, 5, 5}
print(nums)

#=========================================================
#  Convertir secuencia a conjunto
#  No lo genera en orden 
#=========================================================
s= set('Hola')
print(s)
s = set((1,2,3,4,5)) # tupla a conjunto 
print(s)

#=========================================================
#    De diccionario a conjunto: conjunto de llaves
#=========================================================
d = {1:'uno', 2: 'dos'}
s = set(d)
print(s)

s.add(100)
print(s)

s.update(nums)
print(s)

s.remove(100)
print(s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

su = s1|s2   #union
print(su)

si = s1&s2    # Intersecion
print(si)

sr = s1-s2    #Diferencia de conjuntos
print(sr)

sp = s2-s1
print(sp)

ss= s1^s2    # Diferencia simetreica
print(ss)

#=====================================================
#  Uso de diccionarios 
#=====================================================
capitales = {"USA":"Washington D.C", "France":"Paris", "India":"New delhi"}
print(capitales)

#===================================================================
# llave:valor
#===================================================================
#   diccionario vacio
d = {}

# llave entera, valor string
numeros={1:"uno",2:"dos",3:"tres"}

# llave real, valor string
decimales={1.5:"uno y medio", 2.5: "dos y medio", 3.5:"tres y medio"}

# llave tupla, valor string
cosas={("Parker","Reynolds","Camlin"):"pluma", ("LG","Whirpool","Samsung"): "refrigerador"}

# llave string, valor int
romanos = {'I':1, 'II':2,'III':3, 'IV':4, 'V':5}
print(romanos)
print(romanos["I"])

print(capitales.get("India"))
print(capitales.get("India"))

# Reportar llave y valor
for k in capitales:
    print("Key ="+ k +", Value = "+ capitales[k])

# Nuevo dato para el diccionario
capitales["Mexico"] = "CDMX"    
print(capitales)

# Borra dato del diccionario
del capitales["Mexico"] 
print(capitales)

# Borra todo el diccionario
del capitales

# Reportar llaves 
print(romanos.keys())

# Reportar valores 
print(romanos.values())

# Juicio de llave (esta o no esta la llave en el diccionario)
print("I" in romanos)
print("X" in romanos)
print("XX" not in romanos)




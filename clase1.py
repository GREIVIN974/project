# son 4 tipos de variables 
# string
name = "GREIVIN"
last_name = "BERMUDEZ"
# integer
ID = 116270062

# float
CASH = 10.5

# bool
ACTIVE = True


# comparaciones de las variables 
# como verificar si el PIN ingresado por un usuario coincide con su PIn guardado

entered_pin = 1234
expected_pin = 1234

result = entered_pin == expected_pin

print(result
)


# compoaraciones con desigualdad. tenemos que el operador   !=

result_1 = 2 != 2

print(result_1)

one = 1
two = 2
print("-------------------------------------------------")
print(one==two)
print(one != two)



# vamos a hacer  un interrupotor de luz inteligente que apague las 
# luces si de dia y las enciede si es de noche
print("-----------------separador---------------------------------")


is_day = False

lights_on = not is_day

print("daytime")
print("Lights on?")


print("lights on?")
print(lights_on)


# con las comparaciones vamos a hacer un codigo que rastree los datos 
# de ventas en una tienda de pantalones

print("-----------------separador---------------------------------")


stock = 600
jeans_sold = 500
target = 500

target_hit = jeans_sold == target
print("hit jeans sale target")
print(target_hit)


current_stock = stock - jeans_sold
in_stock = current_stock != 0
print("jean in stock:")
print(in_stock)

print(current_stock)

print("-----------------separador---------------------------------")

# podemos usar comparaciones para verificar si un
#  numero es mayaor o menos que otro numero

print(2 < 200)
print(2 > 200)


print(2 <= 200)
print(2 >= 200)


print("-----------------separador---------------------------------")
# comparaciones de cadenas de texto


my_asnwer = "lowr"
solution = "low"
print(my_asnwer == solution)
print(my_asnwer != solution)

# ejercicio de medidor de frecuencia cardiaca, usando comparaciones para verificar si la frecuncia cardiaca es demaciada baja o alta y le diremos al paciente si debe preocuparse.

rit_cardiaco = 77


muy_baja = rit_cardiaco < 60
muy_alto = rit_cardiaco > 100

print("heart rate low?")
print("to low")



print("-----------------separador---------------------------------")

# sumar edades  de hombre y mujeres

hombres = 10
mujeres = 28

suma = hombres + mujeres
print(suma)

print("-----------------separador---------------------------------")

peras_compradas = 200

peras_vendidas = 100

total_de_ventas = peras_compradas - peras_vendidas

print(total_de_ventas)

print("-----------------separador---------------------------------")


hombres = 10
mujeres = 28
mayor_de_edad = hombres >= 18

print("mayor de edad?")

print(mayor_de_edad)


print("-----------------separador---------------------------------")
#  usemos comparaciones de string para etiquetar los datos adquiridos a traves de la encuesta de usauarios de una aplicacion de fitness. verificamos las respuestas de la encuesta de los usuarios con respecto a la frecuncia e intensidad de la actividad, las etiquetaremos y mostraremos los resultados


frecuencia = "una vez a la semana"
intensidad = "baja"
activo = frecuencia == "diaria"
print("el usuario es activo?")
print(activo)
print("el usuario es intenso?")
intenso = intensidad == "alta"
print(intenso)


print(f"la edad de greivin es {hombres} ")


print("-----------------separador---------------------------------")
tel = 87181507

print(f"https://wa.me/506{tel}")






print("-----------------ejercicio 1/2---------------------------------")
#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
#Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre 
# por pantalla el contenido de la variable.

print("HOLA MUNDO")

COMENTARIO = ("HOLA MUNDO")

print(COMENTARIO)

print("-----------------ejercicio 3---------------------------------")
#Escribir un programa que almacene el nombre del usuario en la consola y después de que muestre 
# por pantalla la cadena 
# ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario.

NOM = "EMA"

print(F"!HOLA {NOM}¡ ")


print("-----------------ejercicio 4---------------------------------")
#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritméticas


oper = ("((3+2)/(2*5))**2")

sim = 3+2 

sim2 = 2*5

sim3 = "(1/2)^2"

sim4 = "1/2^2"

sim5 = 1/4

print(oper)


print(f"Simplifica 3+2 = {sim}")


print(f"Simplifica 2*5 = {sim2}")


print(f"Simplifica (5/10)^2 = {sim3}")


print(f" Usa Propiedad de la División Distributiva:{sim4}")





print(sim4)


print(f"El resultado es 1/4 o lo mismo que {sim5}")



print("-----------------ejercicio 5---------------------------------")
# Escribir un programa que pregunte almacene el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.

horas = 8


costo = 2000

supago = horas * costo 

print(f"Digíte cantidad de horas trabajadas ____ {8}. Ahora digíte el costo de cada hora de trabajo___{costo}")

print(f"SU PAGO ES DE {supago}")



print("-----------------ejercicio 6---------------------------------")

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el 
# índice de masa corporal y lo almacene en una variable, y muestre por pantalla 
# la frase Tu índice de masa corporal es <imc> donde <imc> 
# es el índice de masa corporal calculado redondeado con dos decimales.

peso = 90

# variable tipo floar
estat = 1.83


mascop = peso /estat

print(f"Digite su peso en kg__{peso}")
print(f"Digite su estatura en metros__{estat}")
print(f"Tu índice de masa corporal es:{mascop}imc")


print("----------------- ejercicio 7 ---------------------------------")

# Escribir un programa donde almacenas dos números enteros 
ent1 = 100
ent2 = 80

# y muestre por pantalla la <n> entre <m> 
print(ent1)
print("/")
print(ent2)
# da un cociente <c> y un resto <r> donde <n> y <m> son los números almacenados, y <c> y <r> son el 
# cociente y el resto de la división entera respectivamente.


result = ent1 / ent2


print(result)




print("----------------- investigacion  ---------------------------------")
print("----------------- Ejercicio 1  ---------------------------------")
# Escribir un programa que pregunte el nombre completo del usuario en la consola y 
# después muestre por pantalla el nombre completo del usuario tres veces, una con todas 
# las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra 
# del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando
#  mayúsculas y minúsculas como quiera.

nombre_completo = input("Introduce tú nombre completo:")

print(nombre_completo.lower())


print(nombre_completo.upper())


print(nombre_completo.title())

print("----------------- Ejercicio  2 ---------------------------------")
#Escribir un programa que pregunte el nombre del usuario en la consola y
#  un número entero e imprima por pantalla en líneas distintas el nomb re del 
# usuario tantas veces como el número introducido.

nom = input("Ingrese su nombre: ")

numentero = int(input("Ingrese un número entero: "))

for y in range(numentero):
    print(nom)

#En este programa, se utiliza la función input()para pedir al usuario su nombre y un número entero.
#  Luego, el número ingresado se convierte a un entero utilizando la función int(), para poder utilizarlo en un ciclo 
# forque se repetirá el número de veces indicado. Dentro del ciclo, se imprime el nombre del usuario utilizando la función 
# print()en cada iteración.






print("----------------- Ejercicio  3 ---------------------------------")

#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.


nombr = input("DÍGITE SU NOMBRE ")

print(nombr.upper() + "tiene" + str(len(nombr)) + " letras")

#UPPER PARA HACER MAYUSCULAS 
#LEN devuelve un valor entero que indica la cantidad de caracteres en la cadena de entrada
#str se utiliza para representar texto



#LOS PROGRamas inteligentes usan booleanos (true o false) para toamr decisiones sobre si ejecutar lineas de codigo
#u omitirla

print("----------------- SEPARADOR ---------------------------------")










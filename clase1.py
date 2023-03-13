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









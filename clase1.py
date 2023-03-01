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


























# # Ejercicio de edades.

# dia = 2
# mes = 3
# anio = 1888

# anio_actual = 2021
# mes_actual = 3
# dia_actual = 2

# cumple = True

# #Calculo base de edad
# edad = anio_actual - anio

# # Se determina si se cumplio anio
# if mes_actual <= mes and dia_actual < dia:
#     # Si no ha cumplido aun, eliminamos 1 de la edad.
#     edad = edad - 1
#     cumple = False

# # Determina mensaje en base a si ya cumplio anio
# mensaje_cumple = 'Ya cumplio anios'
# if not cumple:
#     mensaje_cumple = 'No ha cumplido anios'

# # Determina a que generaion pertenece
# generacion = ''
# if anio >= 1920 and anio <= 1939:
#     generacion = 'Generacion Silenciosa'
# elif anio >= 1940 and anio <= 1959:
#     generacion = 'Baby Boomers'
# elif anio >= 1960 and anio <= 1979:
#     generacion = 'Generacion X'
# elif anio >= 1980 and anio <= 1989:
#     generacion = 'Generacion Y'
# elif anio >= 1990 :
#     generacion = 'Generacion Z'
# else:
#     generacion = 'La edad no corresponde a una generacion'

# # Salidas
# print('tiene {} anio'.format(edad))
# print(mensaje_cumple)
# print('Pertenece a la generacion: {}'.format(generacion))

# #Ejercicio 1 - While
# numero = 3
# variable_control = 0
# resultado = 0

# while variable_control <= numero:
#     resultado += variable_control
#     variable_control += 1
# print(resultado)

# # Ejercicio 3 - While
# numero_a = 2
# numero_b = 5
# numeros = ''

# num_max = 0
# num_min = 0

# if numero_a > numero_b:
#     num_max = numero_a
#     num_min = numero_b
# else:
#     num_max = numero_b
#     num_min = numero_a

# num_min +=1
# num_max -= 1
# while num_min < num_max:
#     numeros += '{}, '.format(num_min)
#     num_min += 1

# if num_max >= num_min:    
#     numeros += '{}'.format(num_max)

# print('los numeros son: {}'.format(numeros))

#Ejercicio1 - for

import random

numero = random.randint(1,10)

for num in range(1,11):
    resultado = numero * num
    print('{} x {} = {}'.format(numero, num, resultado))
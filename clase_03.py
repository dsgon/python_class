'''
    Clase 03 - Variables , Sintaxis
    Esta es otra line
'''

# # Formateando Strings
# nombre = 'David'
# pais = 'Argentina'
# edad = 33
# #Ejemplo 1 - Mas recomendable
# texto_a = 'Hola QA Minds, mi nombre es: {} y soy de: {} y tengo {} años'.format(nombre,pais,edad)
# print(texto_a)

# #Ejemplo 2 - Mas recomendable
# texto_a = f'Hola QA Minds, mi nombre es: {nombre} y soy de: {pais} y tengo {edad} años'
# print(texto_a)

# #Ejemplo 3 - Menos usada, pero posible
# texto_a = 'Hola QA Minds, mi nombre es: %s y soy de: %s y tengo %s años' % (nombre,pais,edad)
# print(texto_a)

# #Ejemplo 4 - No recomendable
# texto_a = 'Hola QA Minds, mi nombre es: '+ nombre +' y soy de: '+ pais +' y tengo '+str(edad)+' años'
# print(texto_a)

# Condicionales

# # Ejemplo 1
# billetera = 100
# agua = 100
# compra_exitosa = billetera >= agua
# print(compra_exitosa)

# # Ejemplo 2
# billetera = 100
# agua = 100
# compra_exitosa = billetera > agua
# print(compra_exitosa)

# #Ejemplo - 3
# var_a = 2
# var_b = 4
# print(var_a is var_b)
# print(var_a is not var_b)

# Discovery
var_int = 1
var_float = 1.0
var_none = None
var_bool = True
var_str = ''

# print(var_int == var_float) #True
# print(var_int == var_bool) #True
# print(0 == False) #True
# print(0 > var_str)
# print(var_str > var_none)
# print(0 == var_none) #False
# print(1 == var_none) #False

# #Ejercicio Estaciones.
# mes_numero = 'Enero'

# if mes_numero == 'Enero':
#     print('Invierno')
# elif mes_numero == 2:
#     print('Invierno')
# elif mes_numero == 12:
#     print('Invierno')
# else:
#     print('Invalido')

#Ejercicio - Montaña Rusa
altura_permitida = 1.62
edad_permitida = 14

# Edad y Altura no permitida
# p_edad = 12
# p_altura = 1.50

# Edad no permitida y Altura permitida
# p_edad = 12
# p_altura = 1.65

# Edad permitida y Altura no permitida
# p_edad = 18
# p_altura = 1.50

# Edad y Altura permitida
p_edad = 16
p_altura = 1.75

edad_persona = p_edad
altura_persona = p_altura

if edad_persona >= edad_permitida and altura_persona >= altura_permitida:
    print('Puedes subir')
elif edad_persona < edad_permitida and altura_persona < altura_permitida:
    print('No puedes subir por no tener la edad y altura permitida')
elif edad_persona < edad_permitida :
    print('No puedes subir por no tener la edad permitida')
else:
    print('No puedes subir por no tener la altura permitida')
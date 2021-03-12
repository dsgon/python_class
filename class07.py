#Ejercicio 2 - Listas - Forma A

import random

# lista_aleatoria = []

# for value in range (1,10):
#     lista_aleatoria.append(random.randint(1,9))

# print(lista_aleatoria)
# indice = 0
# repetido = False

# lista_aleatoria.sort()
# print(lista_aleatoria)

# while indice < len(lista_aleatoria) - 1 and not repetido:
#     if lista_aleatoria[indice] == lista_aleatoria[indice+1]:
#         print('El numero {} esta repetido'.format(lista_aleatoria[indice]))
#         repetido = True
#     indice += 1

# if not repetido:    
#     print('No hay numeros repetidos')


#Ejercicio 2 - Listas - Forma B
# lista_aleatoria = []

# for value in range (1,10):
#     lista_aleatoria.append(random.randint(1,9))

# print(lista_aleatoria)
# indice = 0
# repetido = False

# while indice < len(lista_aleatoria) and not repetido:
#     value = lista_aleatoria[indice]
#     lista_aleatoria.pop(0)
#     if value in lista_aleatoria:
#         print('El numero {} esta repetido'.format(value))
#         repetido = True
#     lista_aleatoria.append(value)
# if not repetido:    
#     print('No hay numeros repetidos')


# #Ejercicio 2 - Listas - Forma C
# lista = [] 
# for i in range(1,10):
#     lista.append(random.randint(1,9))

# #lista = [1,2,3,4,5,6,7,8,9] 
# print('Mi lista es {} '.format(lista))
           
# repetido = False 
# countador = 0
# while countador < len(lista):
#     if lista.count(lista[countador]) > 1:
#          repetido =  True
#          print("El numero repetido es: {}".format(lista[countador]))
#          break
#     countador += 1


# if not repetido:
#     print("No existen números repetidos")

# Ejercicio 3 - Pocker Planning
pocker_planning = [0,0.5,1,2,3,5,8,13,20,40,100]
pares = 0
divisibles = 0
suma = 0
indice = 0

for number in pocker_planning:
    if number % 2 == 0:
        pares+=1

    if indice > 1 and number % pocker_planning[indice-1] == 0:
        divisibles+=1

    suma+=number
    indice+=1

print('Pares: {}'.format(pares)) 
print('Divisibles: {}'.format(divisibles))
print('Sumatoria: {}'.format(suma))
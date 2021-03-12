# # Modificacion de Listas

# my_list = [4,5,6,7]
# my_list[2] = 0

# # Obtener ultimo valor de una lista
# #print(my_list[len(my_list)-1])

# #Agregar un nuevo item
# my_list.append(10)
# #my_list.append('Hola')

# #print(my_list[3])
# # del my_list[2]
# my_list.pop(2)
# #print(my_list[3])

# # Obtener ultimo valor de una lista con indices negativos
# #print(my_list[-1])

# # Obtener ultimo valor de una lista con indices negativos
# #print(my_list[-2])

# my_list = [4,3,6,1,2,5]
# my_list.reverse()
# #print(my_list)
# my_list.sort()
# #print(my_list)

# for number in my_list:
#     print(number)


# Ejercicio 1 - Listas
import random

numeros = [1,2,3,4,5]
print('el tamaño de la lista es: {}'.format(len(numeros)))

numero = random.randint(1,10)
print('el numero random es: {}'.format(numero))

numeros.append(numero)

indice = 0
     
while indice < len(numeros) and numero <= 5 :
    if numero == numeros[indice]:
        numeros.pop(indice)
        print('El numero se encontraba en la lista y fue eliminado')
        break
    indice+=1

if len(numeros)==6:
    numeros.pop(indice)
    print('El numero no estaba en la lista, por lo que se elimina el primer registro')

print('el nuevo tamaño de la lista es: {}'.format(len(numeros)))
print('la lista es: {}'.format(numeros))
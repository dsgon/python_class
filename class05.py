#import random

# numero = random.randint(1,10)

# print('El numero es: {}'.format(numero))

# for num in range(1,numero+1):
#     print('ESCALERA' * num)

# for num in range(1,10):
#     if num % 2 == 0:
#         print('El numero {} es par.'.format(num))
#         break
#     print('Este numero: {} no es par'.format(num))

# num = 1
# while num % 2 != 0:
#     print('Este numero: {} no es par'.format(num))
#     num +=1
# print('El numero {} es par.'.format(num))

# num = 1
# while num < 10:
#     if num % 2 == 0:
#         print('El numero {} es par.'.format(num))
#         break
#     print('Este numero: {} no es par'.format(num))
#     num +=1

# result = 0
# for num in range (1,10):
#     if num % 2 == 0:
#         continue
#     print(num)
#     result += num
# print(result)

# numero = random.randint(1,20)
# print(numero)
# for num in range (1, 20):
#     print(num)
#     if num != numero:
#         continue
#     print('Los numeros son iguales: {} == {}'.format(numero,num))
#     break

# num = 0
# while num != numero:
#     num += 1
# print('Los numeros son iguales: {} == {}'.format(numero,num)) 

# Ejercicio:
# Imprime todos los numeros del 0 al 99 de dos en dos y que no sean multiplos de 3.

# While Solution
# num = 0
# while num < 100:
#     if num % 3 != 0:
#         print(num)
#     num +=2

# For Solution
# for num in range(0,100,2):
#     if num % 3 != 0:
#         print(num)

# import random

# numero = random.randint(1,20)
# numero *= 2
# num = 2
# result = 1
# print(numero)
# while num != numero:
#     print('Esto se ejecuta {} veces'.format(num-1))
#     result += num
#     num +=1
# print(result)

palabra = 'HolaMundo'
numero = 10
my_lista = [1,2,3,4,5,6]
my_lista.append(8)
print(len(my_lista))

print(my_lista[len(my_lista)-1])
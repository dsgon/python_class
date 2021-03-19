
my_dict = {
    'nombre' : 'David',
    'apellido' : 'Gonzalez',
    'edad' : 33
}

#print(my_dict['apellido'])
#print(my_dict.get('apellido'))
#print()

my_dict['apellido'] = 'Hernandez'
#print(my_dict['apellido'])

#print(len(my_dict))
#print(my_dict)
my_dict['pais'] = 'Argentina'

#print(my_dict)


#hobbie = my_dict.pop('hobbie','No tiene hobbie')
# #Validacion por medio de 'in'
# if not 'hobbie' in my_dict:
#     print('No tiene hobbie')
# else:
#     print('Tiene hobbie')

# Validacion por medio de get()
if my_dict.get('hobbie') is None:
    print('No tiene hobbie')
else:
    print('Tiene hobbie')

#print(my_dict)

alumnos = {
    'alumnos':[
        {
            'nombre' : 'Valentina',
            'edad' : 20,
            'pais' : 'Venezuela'
        },
        {
            'nombre' : 'Oscar',
            'edad' : 34,
            'pais' : 'Mexico'
        },
        {
            'nombre' : 'Viridiana',
            'edad' : 28,
            'pais' : 'Mexico'
        }
    ]
}

list_alumnos = alumnos['alumnos']
nuevo_alumno = {
    'nombre' : 'Gaby',
    'edad' : 28,
    'pais' : 'Mexico'
}
list_alumnos.append(nuevo_alumno)

#alumnos['alumnos'].append({'nombre' : 'Gaby','edad' : 28,'pais' : 'Mexico'})

# for alumno in alumnos['alumnos']:
#     print('---- Nuevo alumno ----')
#     for key, value in alumno.items():
        # print('Key = {} y Value = {}'.format(key,value))


# for key in alumnos['alumnos'][0].keys():
#     print('Key = {}'.format(key))

# for value in alumnos['alumnos'][3].values():
#     print('Value = {}'.format(value))

agenda = {'contactos':[]}

opcion = input('Ingrese una opcion: "a" para agregar, "b" para buscar, "e" para eliminar, "v" para visualizar o "s" para salir\n')
while opcion != 's':

    if opcion == 'a':
        print('Agregar Contacto')
        nombre = input('ingrese el nombre a registrar\n')
        telefono = input('ingrese el telefono a registrar\n')
        email = input('ingrese el mail a registrar\n')
        contacto ={
            'nombre' : nombre,
            'numero telefonico' : telefono,
            'mail' : email
        }
        agenda['contactos'].append(contacto)

    elif opcion == 'b':
        print('Buscar Contacto')
        nombre = input('ingrese el nombre a buscar\n')
        contactos = []
        for contacto in agenda['contactos']:
            if nombre in contacto.values():
                contactos.append(contacto)
        
        for contacto in contactos:
            for key, value in contacto.items():
                print('{} : {}'.format(key,value))
    elif opcion == 'e':
        print('Eliminar Contacto')
    elif opcion == 'v':
        print('Visualizar Contactos')
        for contacto in agenda['contactos']:
            print('---- Contacto ----')
            for key, value in contacto.items():
                print('{} - {}'.format(key,value))
    else:
        print('Opcion invalida, ingrese una opcion valida')
    opcion = input('Ingrese una opcion: "a" para agregar, "b" para buscar, "e" para eliminar, "v" para visualizar o "s" para salir\n')



# agenda = {
#     'contactos' : []
# }

# opcion = int(input('''Ingrese una opcion (1 para guardar un contacto, 2 para visualizar agenda, 
# 3 para buscar un contacto, 4 para eliminar un contacto, 0 para salir)\n'''))

# while opcion != 0:
#     if opcion == 1:
#         print('---- Agregar Contacto ----')
#         nombre = input('Ingrese nombre del contacto\n')
#         numero_telefonico = input('Ingrese numero de telefono del contacto\n')
#         email = input('Ingrese email del contacto\n')
#         contacto = {
#             'nombre' : nombre,
#             'numero' : numero_telefonico,
#             'email' : email
#         }
#         agenda['contactos'].append(contacto)
#         opcion = int(input('''Ingrese una opcion (1 para guardar un contacto, 2 para visualizar agenda,
# 3 para buscar un contacto, 4 para eliminar un contacto, 0 para salir)\n'''))
#     elif opcion == 2:
#         print('---- Listar Agenda ----')
#         for contacto in agenda['contactos']:
#             print('---- Contacto ----')
#             for key, value in contacto.items():
#                 print('{} : {}'.format(key,value))
#         opcion = int(input('''Ingrese una opcion (1 para guardar un contacto, 2 para visualizar agenda, 
# 3 para buscar un contacto, 4 para eliminar un contacto, 0 para salir)\n'''))
#     elif opcion == 3:
#         print('---- Buscar Contacto ----')
#         nombre = input('Ingrese nombre del contacto\n')
#         contactos = []
#         for contacto in agenda['contactos']:
#             if nombre in contacto.values():
#                 contactos.append(contacto)
#         print('---- Contacto ----')
#         for contacto in contactos:
#             for key, value in contacto.items():
#                 print('{} : {}'.format(key,value))
#         opcion = int(input('''Ingrese una opcion (1 para guardar un contacto, 2 para visualizar agenda,
# 3 para buscar un contacto, 4 para eliminar un contacto, 0 para salir)\n'''))
#     elif opcion == 4:
#         print('---- Eliminar Contacto ----')
#         nombre = input('Ingrese nombre del contacto\n')
#         count = 0
#         contactos = agenda['contactos']
#         while count < len(contactos):
#             contacto = agenda['contactos'][count]
#             if nombre in contacto.values():
#                 opcion = int(input('Desea eliminar el contacto: {} - {} = {} ? Presione 1 para confirmar o 0 para cancelar\n'.\
#                     format(contacto['nombre'],contacto['numero'],contacto['email'])))
#                 if opcion == 1:
#                     index = contactos.index(contacto)
#                     contactos.pop(index)
#                     print('Se ha eliminado el contacto.')
#                     break
#             count+=1
#         opcion = int(input('''Ingrese una opcion (1 para guardar un contacto, 2 para visualizar agenda,
# 3 para buscar un contacto, 4 para eliminar un contacto, 0 para salir)\n'''))
#     else:
#         opcion = int(input('''Opcion Invalida. Ingrese una opcion (1 para guardar un contacto, 2 para visualizar agenda,
# 3 para buscar un contacto, 4 para eliminar un contacto, 0 para salir)\n'''))
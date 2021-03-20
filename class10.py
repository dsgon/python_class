'''
    Clase 10 - Archivos
'''

# # file = open('mi_archivo.txt','a')
# # file.write('Hola, este es mi primer archivo desde Python.')
# # file.close()

# file = open('mi_archivo.txt','w')
# file.write('Hola, acabo de remplazar todo! 01\n')
# file.write('Hola, acabo de remplazar todo! 02\n')
# file.write('Hola, acabo de remplazar todo! 03\n')
# file.write('Hola, acabo de remplazar todo! 04\n')
# file.write('Hola, acabo de remplazar todo! 05')
# file.close()

# file = open('mi_archivo.txt','r')
# #file.write('Hola, acabo de remplazar todo!')
# #print(file.read())
# # print(file.readline())
# # print(file.readline())
# # print(file.readline())

# for line in file.readlines():
#     print(line[:-1])
# file.close()


#Ejercicio - Agenda

agenda_file = 'mi_agenda.csv'

opcion = int(input('''Ingrese una opcion (1 para guardar un contacto, 2 para visualizar agenda, 
3 para buscar un contacto, 4 para eliminar un contacto, 0 para salir)\n'''))

while opcion != 0:
    file = None
    if opcion == 1:
        print('---- Agregar Contacto ----')
        nombre = input('Ingrese nombre del contacto\n')
        numero_telefonico = input('Ingrese numero de telefono del contacto\n')
        email = input('Ingrese email del contacto\n')
        file = open(agenda_file,'a')
        file.write('{},{},{}\n'.format(nombre,numero_telefonico,email))
    elif opcion == 2:
        print('---- Listar Agenda ----')
        file = open(agenda_file,'r')
        for contacto in file.readlines():
            print('---- Contacto ----')
            contacto_data = contacto.split(',')
            print('nombre : {}'.format(contacto_data[0]))
            print('numero : {}'.format(contacto_data[1]))
            print('e-mail : {}'.format(contacto_data[2]))
    elif opcion == 3:
        print('---- Buscar Contacto ----')
        nombre = input('Ingrese nombre del contacto\n')
        file = open(agenda_file,'r')
        find = False
        for contacto in file.readlines():
            if nombre in contacto:
                print('---- Contacto ----')
                contacto_data = contacto.split(',')
                print('nombre : {}'.format(contacto_data[0]))
                print('numero : {}'.format(contacto_data[1]))
                print('e-mail : {}'.format(contacto_data[2]))
                find = True
        if not find:
            print('No existe un contacto con ese nombre')
    elif opcion == 4:
        print('---- Eliminar Contacto ----')
        nombre = input('Ingrese nombre del contacto\n')
        file = open(agenda_file,'r')
        contactos = []
        deleted = False
        for contacto in file.readlines():
            if nombre in contacto and not deleted:
                contacto_data = contacto.split(',')
                opcion = int(input('Desea eliminar el contacto: {} - {} = {} ? Presione 1 para confirmar o 0 para cancelar\n'.\
                    format(contacto_data[0],contacto_data[1],contacto_data[2])))
                if opcion == 0:
                    contactos.append(contacto)
                else:
                    deleted = True
            else:    
                contactos.append(contacto)
        file = open(agenda_file,'w')
        for contacto in contactos:
            file.write(contacto)

        if deleted:
            print('Contacto eliminado')
    else:
       print('Opcion Invalida.\n')

    if file is not None:
        file.close()
    opcion = int(input('''Ingrese una opcion (1 para guardar un contacto, 2 para visualizar agenda,
    3 para buscar un contacto, 4 para eliminar un contacto, 0 para salir)\n'''))

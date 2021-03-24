
agenda_file = 'mi_agenda.csv'

# Archivos 'Clasico'
# # file = open(agenda_file,'r')
# # file.read()
# # file.close()

# # With
# with open(agenda_file,'r') as file:
#     print(file.read())
    

# #Json

# import json

# json_file = 'mi_archivo_json.json'

# lista_contactos = []

# # Lectura de Archivo
# with open(json_file,'r') as file:
#     data = json.load(file) # data es un diccionario
#     for contacto in data['contactos']: # data['contactos'] es una lista y contacto es un diccionario
#         lista_contactos.append(contacto)
#         for key, value in contacto.items():
#             print('{} : {}'.format(key,value))

# #Escritura de Archivo
# with open(json_file,'w') as file2:
#     new_contact = {
#         "nombre": "Philco",
#         "telefono" : "74125896",
#         "mail" : "philco@mail.com"
#     }
#     lista_contactos.append(new_contact)
#     new_data = {}
#     new_data['contactos'] = lista_contactos
#     json.dump(new_data,file2)


# with open(json_file,'r') as file:
#     data = json.load(file) # data es un diccionario
#     for contacto in data['contactos']: # data['contactos'] es una lista y contacto es un diccionario
#         lista_contactos.append(contacto)
#         for key, value in contacto.items():
#             print('{} : {}'.format(key,value))

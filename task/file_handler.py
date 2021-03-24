import json

__usuarios_filename = 'usuarios.json'

def exportar_usuarios(usuarios):
    dict_usuarios = __usuarios_to_dict(usuarios)
    with open(__usuarios_filename,'w') as file:
        json.dump(dict_usuarios,file)
        print('Usuarios exportados en el archivo: {}'.format(__usuarios_filename))

def __usuarios_to_dict(usuarios):
    dict_usuarios = {}
    list_usuarios = []
    for usuario in usuarios:
        dict_usuario = {}
        dict_usuario['nombre'] = usuario.get_nombre()
        dict_usuario['email'] = usuario.get_email()
        list_usuarios.append(dict_usuario)
    dict_usuarios['usuarios'] = list_usuarios
    return dict_usuarios
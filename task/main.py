from task.usuario import Usuario
from task.tarea import Tarea
from task import file_handler as fh

opcion = int(input('''Ingrese una opcion (1 para crear un usuario, 2 para exportar usuarios, 3 para buscar un usuario
4 para crear una tarea, 5 para ..., 0 para salir)\n'''))

usuarios = []
tareas = []

def crear_usuario():
    print('---- Crear Usuario ----')
    nombre = input('Ingrese nombre del usuario\n')
    email = input('Ingrese email del usuario\n')
    usuarios.append(Usuario(nombre,email))

def export_usuarios():
    print('---- Exportar Usuarios ----')
    opcion = int(input('Desea exportar los usuarios? Presione 1 para confirmar o 0 para cancelar\n'))
    if opcion==1:
        fh.exportar_usuarios(usuarios)

def buscar_usuario():
    print('---- Buscar Usuario ----')
    email = input('Ingrese email del usuario\n')
    for usuario in usuarios:
        if usuario.get_email()==email:
            return usuario
    print('No existe un usuario con ese mail')
    return None

def print_user_data(usuario):
    print('---- Usuario ----')
    print('Nombre: {}'.format(usuario.get_nombre()))
    print('Email : {}'.format(usuario.get_email()))
    

while opcion != 0:

    if opcion==1:
        crear_usuario()

    elif opcion==2:
        export_usuarios()

    elif opcion==3:
        usuario = buscar_usuario()
        print_user_data(usuario)

    elif opcion==4:
        print('---- Crear Tarea ----')
        titulo = input('Ingrese titulo de la tarea\n')
        descripcion = input('Ingrese una descripcion de la tarea\n')
        prioridad = int(input('Ingrese una prioridad de la tarea(valores del 1 al 5 siendo 1 baja y 5 alta)\n'))
        usuario = None
        while usuario is None:
            usuario = buscar_usuario()
        tarea = Tarea(titulo,descripcion,prioridad,usuario)
        tareas.append(tarea)

    opcion = int(input('''Ingrese una opcion (1 para crear un usuario, 2 para exportar usuarios, 3 para buscar un usuario
4 para crear una tarea, 5 para ..., 0 para salir)\n'''))


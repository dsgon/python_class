__file_name = 'ejercicio_poo.txt'

def guardar_dato(texto,modo_file):
    with open(__file_name,modo_file) as file:
        file.write(texto)
    
def get_file_name():
    return __file_name


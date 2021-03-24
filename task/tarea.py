class Tarea:

    BACKLOG = 'Backlog'
    TODO = 'ToDo'
    DOING = 'Doing'
    RESOLVED = 'Resolved'

    def __init__(self, titulo, descripcion, prioridad, usuario):
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__prioridad = prioridad
        self.__usuario = usuario
        self.__estado = self.BACKLOG

    def get_titulo(self):
        return self.__titulo

    def get_descripcion(self):
        return self.__descripcion

    def get_prioridad(self):
        return self.__prioridad

    def get_usuario(self):
        return self.__usuario

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado
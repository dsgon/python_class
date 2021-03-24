from poo.motor import Motor

class Terrestre:

    __motor = Motor()
    __neumaticos = 0

    def set_neumaticos(self,neumaticos):
        if neumaticos == 4:
            self.__neumaticos = neumaticos
        else:
            raise AttributeError('El Auto debe tener 4 neumaticos')

    def get_neumaticos(self):
        return self.__neumaticos

    def get_nombre_motor(self):
        return self.__motor.get_nombre()
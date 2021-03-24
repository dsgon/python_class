from poo.terrestre import Terrestre

class Car(Terrestre):   

    def __init__(self,marca,color):
        self.__marca = marca
        self.__color = color
        self.set_neumaticos(4)

    def __set_color(self,color):
        self.__color = color

    def get_marca(self):
        return self.__marca

    def get_color(self):
        return self.__color


    

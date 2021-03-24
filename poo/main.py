from poo.car import Car
from poo import file_handler as fh 
# auto = Car('Ferrari', 'Rojo')

# print(auto.get_marca())
# print(auto.get_color())
# print(auto.get_neumaticos())
# print(auto.get_color())

auto = Car('Fiat', 'Negro')
fh.guardar_dato(auto.get_nombre_motor(),'a')

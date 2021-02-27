'''
    Generar mediante la librea de datetime la fecha del dia de hoy
'''
#Importo la libreria datetime
import datetime

hoy = datetime.datetime\
    .now().day # obtiene el valor del dia de hoy

#Imprime el valor de hoy
print(hoy) 
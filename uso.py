#el * significa que pasamos todo lo del modulo a el archivo
from Funciones_matematicas import *
from  atleta import Ciclista

#importamos de un paquete, el modulo Persona
from Modulo.llamado import Persona

persona1 = Persona()
print(sumar(1, 2))

print(resta(5, 2))

at = Ciclista('ruta')
print(at)
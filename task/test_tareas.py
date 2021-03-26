import pytest
from task.tarea import Tarea
from task.usuario import Usuario
from task import file_handler, main
import os

@pytest.mark.skip
def test_suma_valida():
    num_a = 2
    num_b = 2
    expected_result = 4
    assert expected_result == suma(num_a,num_b) , 'Los numeros no son iguales'

@pytest.mark.skip
def test_suma_invalida():
    num_a = 3
    num_b = 2
    expected_result = 4
    assert expected_result != suma(num_a,num_b) , 'Los numeros son iguales'

@pytest.mark.skip
def test_tarea():
    titulo = 'Mi Titulo Test'
    descripcion = 'Descripcion Test'
    prioridad = 1
    usuario = Usuario('David','david@mail.com')
    estado = 'backlog'
    tarea = Tarea(titulo,descripcion,prioridad,usuario)

    assert titulo == tarea.get_titulo() , 'El titulo no coincide'
    assert descripcion == tarea.get_descripcion() , 'El descripcion no coincide'
    assert prioridad == tarea.get_prioridad() , 'El prioridad no coincide'
    assert isinstance(tarea.get_usuario(),Usuario) , 'El usuario no es de tipo Usuario'
    assert estado == tarea.get_estado() , 'El estado no coincide'

@pytest.mark.skip
def test_pass():
    assert True

@pytest.mark.skip
def test_export_users():
    usuarios = [Usuario('a','a@mail.com'),Usuario('b','b@mail.com')]
    file_handler.exportar_usuarios(usuarios)
    assert os.path.isfile('usuarios.json')

def test_input():
    usuario = main.usuarios[0]
    assert 'David' == usuario.get_nombre()




def suma(num_a,num_b):
    return num_a + num_b
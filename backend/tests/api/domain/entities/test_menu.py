import typing

from api.domain.entities import (
    Menu
)


def create_menu() -> Menu:
    return Menu(id = 1, descripcion = 'test', entrada = 'entrada',  
                ensalada = 'ensalada', plato_fondo = 'plato_fondo', postre = 'postre',
                fecha_registro = '2021-01-01', usuario_creacion_id = 1, 
                fecha_menu = '2021-01-01', status_id = 1, status_descripcion = "Mantencion", orden = 1)


def test_all_attributos():
    menu = create_menu()

    assert menu.id == 1
    assert menu.descripcion == 'test'
    assert menu.entrada == 'entrada'
    assert menu.ensalada == 'ensalada'
    assert menu.plato_fondo == 'plato_fondo'
    assert menu.postre == 'postre'
    assert menu.fecha_registro == '2021-01-01'
    assert menu.usuario_creacion_id == 1
    assert menu.fecha_menu == '2021-01-01'
    assert menu.status_id == 1
    assert menu.orden == 1
    menu.setStatus(2)
    assert menu.status_id == 2
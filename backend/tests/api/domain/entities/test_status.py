import typing

from api.domain.entities import (
    Status
)


def create_status() -> Status:
    return Status(id = 1, descripcion = 'test')


def test_all_attributos():
    status = create_status()

    assert status.id == 1
    assert status.descripcion == 'test'

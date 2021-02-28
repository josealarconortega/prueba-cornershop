class MultiplePerfilSerializer:

    @staticmethod
    def serialize(menus):
        return [PerfilSerializer.serialize(menu) for menu in menus]

class PerfilSerializer:

    @staticmethod
    def serialize(menu):
        return {
                'id': menu.id,
                'descripcion': menu.descripcion
            }


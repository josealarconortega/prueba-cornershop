from django.contrib import admin

# Register your models here.
from api.models import *

admin.site.register(Menu)
admin.site.register(Perfil)
admin.site.register(Usuario)
admin.site.register(UsuarioMenu)
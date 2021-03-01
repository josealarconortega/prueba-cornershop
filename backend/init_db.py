import os, sys
sys.path.append('/config')

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
import django
django.setup()

from api.models import Status, Perfil, Usuario
import json
from datetime import date, datetime
import hashlib 

perfil_mantenimiento = Perfil.objects.create(descripcion='Mantenimiento')
perfil_empleado = Perfil.objects.create(descripcion='Empleado')

Status.objects.create(descripcion='Registrado')
Status.objects.create(descripcion='Confirmado')
with open(os.path.dirname(__file__) + "/test_user.json") as f:
    usuariosJSON = json.load(f)
    f.close()
for usuario in usuariosJSON:
    Usuario.objects.create(rut = usuario['rut'], nombre = usuario['nombre'], email = usuario['email'], fecha_registro = datetime.now(), 
        uid = usuario['uid'],perfil = perfil_mantenimiento, password = hashlib.md5(usuario['password'].encode()).hexdigest())
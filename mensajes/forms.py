from django.forms import ModelForm
from models import Mensaje

class MensajeForm(ModelForm):
    class Meta:
        model = Mensaje
        fields = fields = ('titulo', 'fecha', 'cuerpo', 'imagen_path','destinatario_usuario',)
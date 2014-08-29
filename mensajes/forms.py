from django.forms import ModelForm
from models import Mensaje

class MensajeForm(ModelForm):
    class Meta:
        model = Mensaje
        fields = '__all__'
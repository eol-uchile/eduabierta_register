from .models import EduabiertaInfo
from django.forms import ModelForm

class EduabiertaInfoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EduabiertaInfoForm, self).__init__(*args, **kwargs)
        self.fields['phone'].error_messages = {
            "required": "Por favor indique su numero de telefono.",
            "invalid": "Numero de telefono invalido"
        }

    class Meta(object):
        model = EduabiertaInfo
        fields = ('phone',)

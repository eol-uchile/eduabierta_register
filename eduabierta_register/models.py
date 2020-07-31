from django.conf import settings
from django.db import models

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class EduabiertaInfo(models.Model):
    user = models.OneToOneField(USER_MODEL, null=False, on_delete=models.CASCADE)

    phone = models.CharField(verbose_name="Numero de Telefono", max_length=30, blank=False)

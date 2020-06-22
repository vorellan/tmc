from django.db import models


class Credito(models.Model):
    monto_uf = models.DecimalField(max_digits=7, decimal_places=2)
    plazo = models.IntegerField(blank=True, null=False)
    fecha = models.DateField("Fecha", auto_now_add=False)

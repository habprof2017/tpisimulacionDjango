from django.db import models


class VariableLote1(models.Model):
    valor = models.FloatField(max_length=9, null=False, blank=True)

    def __str__(self):
        return str(self.valor)

    class Meta:
        ordering = ['-id']


class VariableLote2(models.Model):
    valor = models.FloatField(max_length=9, null=False, blank=True)

    def __str__(self):
        return str(self.valor)

    class Meta:
        ordering = ['-id']

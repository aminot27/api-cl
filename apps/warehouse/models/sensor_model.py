from django.db import models

from master_serv.models.base_model import BaseModel


class Sensor(BaseModel):
    sensor_id = models.AutoField(primary_key=True)
    system_name = models.CharField(max_length=255, verbose_name="Nombre del Sistema")
    data_cloro = models.CharField(max_length=10, verbose_name="Dato de Cloro")
    data_turbidez = models.CharField(max_length=10, verbose_name="Dato de Turbidez")

    class Meta:
        verbose_name = "Dato de Tesis Electrónica"
        verbose_name_plural = "Datos de Tesis Electrónicas"

    def __str__(self):
        return self.system_name
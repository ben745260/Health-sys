from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, DO_NOTHING, SET_NULL
from django.db.models.expressions import F

# Create your models here.
class HealthData(models.Model):
    data_temperature = models.FloatField(max_length=5)
    data_heartBeat = models.FloatField(max_length=5)
    data_bloodPressure_sys = models.FloatField(max_length=5)
    data_bloodPressure_dia = models.FloatField(max_length=5)
    data_spo2 = models.FloatField(max_length=5)
    saveDate = models.DateTimeField("date punished",default=datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
    remark = models.TextField(blank=True, max_length=8192)
    def __str__(self):
        return f"{self.id}: {self.saveDate} Remark:{self.remark} | {self.data_temperature}, {self.data_heartBeat}, {self.data_bloodPressure_sys}/{self.data_bloodPressure_dia}, {self.data_spo2}"
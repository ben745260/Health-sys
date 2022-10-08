from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, DO_NOTHING, SET_NULL
from django.db.models.expressions import F

# Create your models here.
class HealthData(models.Model):
    data_temperature = models.CharField(max_length=32)
    data_heartBeat = models.CharField(max_length=32)
    data_bloodPressure = models.CharField(max_length=32)
    remark = models.TextField(max_length=8192)
    saveDate = models.DateTimeField("date punished",default=datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
    
    def __str__(self):
        return f"{self.id}: {self.saveDate} Remark:{self.remark}"
from django.db import models
from datetime import datetime

# Create your models here.
class HealthData(models.Model):
    data_temperature =models.CharField(max_length=32)
    data_heartBeat =models.CharField(max_length=32)
    data_bloodPressure =models.CharField(max_length=32)
    remark= models.TextField(max_length=8192)
    saveDate = models.DateTimeField("date punished",default=datetime.now())
    
    def _str_(self):
        return f"{self.id}: {self.saveDate}"
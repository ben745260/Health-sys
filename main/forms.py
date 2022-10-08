from django import forms
from .models import HealthData


class HealthDataForm(forms.ModelForm):
    class Meta:
        model = HealthData
        fields = ('data_temperature','data_heartBeat','data_bloodPressure','remark')
        labels = {
                'data_temperature': 'Temperature',
                'data_heartBeat': 'HeartBeat',
                'data_bloodPressure': 'BloodPressure',
                'remark': 'Remark',
            }
        
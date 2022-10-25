from django import forms
from .models import HealthData


class HealthDataForm(forms.ModelForm):
    class Meta:
        model = HealthData
        fields = ('data_temperature','data_heartBeat','data_bloodPressure_sys','data_bloodPressure_dia','remark')
        labels = {
                'data_temperature': 'Temperature',
                'data_heartBeat': 'HeartBeat',
                'data_bloodPressure_sys': 'Blood Pressure',
                'remark': 'Remark',
            }
        
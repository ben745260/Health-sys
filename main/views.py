from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models.expressions import F

import numpy as np
from datetime import datetime as dt


from .forms import HealthDataForm
from .models import HealthData

def homepage(request):
    healthDatas = HealthData.objects.all()
    form = HealthDataForm()
    status = 0
    if request.method == 'POST':
        form = HealthDataForm(request.POST)
        if form.is_valid():
            form.save()
            status = 1
            messages.success(request, f"New Data Saved")
            return redirect('/')            

    return render(request = request,
                  template_name='main/home.html',
                  context = {
                    'form':form,
                    'healthDatas':healthDatas,
                  })
# ===============================================================================================

def datapage(request):
  healthDatas = HealthData.objects.all()
  # Array[][0]= value, Array[][1]= day, Array[][2]= month, Array[][3]= year
  temp_perTime = [[0]*(4) for i in range(int(HealthData.objects.latest('id').id)+1)]
  HB_perTime = [[0]*(4) for i in range(int(HealthData.objects.latest('id').id)+1)]
  BP_sys_perTime = [[0]*(4) for i in range(int(HealthData.objects.latest('id').id)+1)]
  BP_dia_perTime = [[0]*(4) for i in range(int(HealthData.objects.latest('id').id)+1)]


  ImportDatas = HealthData.objects.order_by('saveDate')

  for data in ImportDatas:
    dataID = data.id
    temp_perTime[dataID][0] = float(data.data_temperature)
    temp_perTime[dataID][1] = int(data.saveDate.day)
    temp_perTime[dataID][2] = int(data.saveDate.month)
    temp_perTime[dataID][3] = int(data.saveDate.year)
    # =======================
    HB_perTime[dataID][0] = float(data.data_heartBeat)
    HB_perTime[dataID][1] = int(data.saveDate.day)
    HB_perTime[dataID][2] = int(data.saveDate.month)
    HB_perTime[dataID][3] = int(data.saveDate.year)
    # =======================
    BP_sys_perTime[dataID][0] = float(data.data_bloodPressure_sys)
    BP_sys_perTime[dataID][1] = int(data.saveDate.day)
    BP_sys_perTime[dataID][2] = int(data.saveDate.month)
    BP_sys_perTime[dataID][3] = int(data.saveDate.year)
    # =======================
    BP_dia_perTime[dataID][0] = float(data.data_bloodPressure_dia)
    BP_dia_perTime[dataID][1] = int(data.saveDate.day)
    BP_dia_perTime[dataID][2] = int(data.saveDate.month)
    BP_dia_perTime[dataID][3] = int(data.saveDate.year)


  return render(request = request,
                template_name='main/data.html',
                context = {
                  'healthDatas': healthDatas,
                  'ImportDatas' : ImportDatas,
                  'temp_perTime' : temp_perTime,
                  'HB_perTime' : HB_perTime,
                  'BP_sys_perTime' : BP_sys_perTime,
                  'BP_dia_perTime' : BP_dia_perTime,
                })
# ===============================================================================================

def reportpage(request):
    healthDatas = HealthData.objects.all()
    newestData = HealthData.objects.order_by('-id')[0]
    temp = newestData.data_temperature 
    HB = newestData.data_heartBeat
    BP_sys = newestData.data_bloodPressure_sys
    BP_dia = newestData.data_bloodPressure_dia

    # =======================
    if temp <= 35.0:
      temp_message = "Hypothermia"
    elif temp >35 and temp <=37.5:
      temp_message = "Normal"
    elif temp >37.5 and temp <=40:
      temp_message = "Fever"
    elif temp >35 and temp <=37.5:
      temp_message = "Hyperpyrexia"
    else:
      temp_message = "error"
    # =======================
    if HB < 60 :
      HB_message = "Bradycardia"
    elif temp >=60 and temp <=100:
      HB_message = "Normal"
    elif temp >100:
      HB_message = "Tachycardia"
    else:
      HB_message = "error"
    

    
    return render(request = request,
                  template_name='main/report.html',
                  context = {
                    'healthDatas':healthDatas,
                    'newestData' : newestData,
                    'temp_message' : temp_message,
                    'HB_message' : HB_message,
                  })

# ===============================================================================================

def testpage(request):
    healthDatas = HealthData.objects.all()
    newestData = HealthData.objects.order_by('-id')[0]
    return render(request = request,
                  template_name='main/test.html',
                  context = {
                    'healthDatas': healthDatas,
                    'newestData' : newestData,
                  })




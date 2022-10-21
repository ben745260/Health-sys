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
            messages.success(request, f"New Data Added")
            return redirect('/')

    return render(request = request,
                  template_name='main/home.html',
                  context = {
                    'form':form,
                    'healthDatas':healthDatas,
                    'status': status
                  })
# ===============================================================================================

def datapage(request):
  healthDatas = HealthData.objects.all()
  # Array[][0]= value, Array[][1]= day, Array[][2]= month, Array[][3]= year
  temp_perTime = [[0]*(4) for i in range(int(HealthData.objects.latest('id').id)+1)]
  HB_perTime = [[0]*(4) for i in range(int(HealthData.objects.latest('id').id)+1)]
  BP_perTime = [[0]*(4) for i in range(int(HealthData.objects.latest('id').id)+1)]

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
    BP_perTime[dataID][0] = float(data.data_bloodPressure)
    BP_perTime[dataID][1] = int(data.saveDate.day)
    BP_perTime[dataID][2] = int(data.saveDate.month)
    BP_perTime[dataID][3] = int(data.saveDate.year)

  return render(request = request,
                template_name='main/data.html',
                context = {
                  'healthDatas': healthDatas,
                  'ImportDatas' : ImportDatas,
                  'temp_perTime' : temp_perTime,
                  'HB_perTime' : HB_perTime,
                  'BP_perTime' : BP_perTime,
                })


# ===============================================================================================

def testpage(request):
    healthDatas = HealthData.objects.all()
    return render(request = request,
                  template_name='main/test.html',
                  context = {
                    'healthDatas':healthDatas,
                  })




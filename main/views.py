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
  temp_value_arr = []
  all_date_arr = []
  all_date_arr1 = []
  years = int(dt.now().date().year)-2020
  # Array[year][month]
  numCounter = [[0]*(13) for i in range(years)]
  temp_monthly = [[0]*(13) for i in range(years)]
  HB_monthly = [[0]*(13) for i in range(years)]
  BP_monthly = [[0]*(13) for i in range(years)]
  month_labels = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']

  for healthData in healthDatas:
    temp_value_arr.append(float(healthData.data_temperature))
    all_date_arr1.append(healthData.saveDate.month)

    all_date_arr = np.array(all_date_arr1, dtype = dt)

  # calulate aveage healthData monthly and yearly
  for healthData in healthDatas:
    arr_year = int(healthData.saveDate.year) - 2021
    arr_month = int(healthData.saveDate.month)
    numCounter[arr_year][arr_month] += 1
    temp_monthly[arr_year][arr_month] += float(healthData.data_temperature)
    HB_monthly[arr_year][arr_month] += float(healthData.data_heartBeat)
    BP_monthly[arr_year][arr_month] += float(healthData.data_bloodPressure)

  # Get Average
  for year in range(years):
    for month in range(13):
      if numCounter[year][month] != 0:
        temp_monthly[year][month] = round(temp_monthly[year][month]/numCounter[year][month],2)
        HB_monthly[year][month] = round(HB_monthly[year][month]/numCounter[year][month],2)
        BP_monthly[year][month] = round(BP_monthly[year][month]/numCounter[year][month],2)

  return_years = []
  temp=1
  for i in range(years):
      return_years.append(2020+temp)
      temp +=1

  return render(request = request,
                template_name='main/data.html',
                context = {
                  'healthDatas': healthDatas,
                  'temp_value_arr': temp_value_arr,
                  'all_date_arr': all_date_arr,
                  'temp_monthly' : temp_monthly,
                  'HB_monthly' : HB_monthly,
                  'BP_monthly' : BP_monthly,
                  'numCounter' : numCounter,
                  'month_labels' : month_labels,
                  'return_years' : return_years,
                })


# ===============================================================================================

def testpage(request):
    healthDatas = HealthData.objects.all()
    return render(request = request,
                  template_name='main/test.html',
                  context = {
                    'healthDatas':healthDatas,
                  })




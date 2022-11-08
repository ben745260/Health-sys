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
  Spo2_perTime = [[0]*(4) for i in range(int(HealthData.objects.latest('id').id)+1)]


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
    # =======================
    Spo2_perTime[dataID][0] = float(data.data_spo2)
    Spo2_perTime[dataID][1] = int(data.saveDate.day)
    Spo2_perTime[dataID][2] = int(data.saveDate.month)
    Spo2_perTime[dataID][3] = int(data.saveDate.year)


  return render(request = request,
                template_name='main/data.html',
                context = {
                  'healthDatas': healthDatas,
                  'ImportDatas' : ImportDatas,
                  'temp_perTime' : temp_perTime,
                  'HB_perTime' : HB_perTime,
                  'BP_sys_perTime' : BP_sys_perTime,
                  'BP_dia_perTime' : BP_dia_perTime,
                  'Spo2_perTime' : Spo2_perTime,
                })
# ===============================================================================================

def reportpage(request):
    healthDatas = HealthData.objects.all()
    newestData = HealthData.objects.order_by('-id')[0]
    temp = newestData.data_temperature 
    HB = newestData.data_heartBeat
    BP_sys = newestData.data_bloodPressure_sys
    BP_dia = newestData.data_bloodPressure_dia
    Spo2 = newestData.data_spo2
    temp_advice = []
    HB_advice = []
    BP_advice = []
    Spo2_advice = []

    # =======================
    if temp == 0:
      temp_message = "Temperature Not Yet Upload"
      temp_advice.append("You have not upload this data.")
    elif temp <= 35.0:
      temp_message = "Hypothermia"
      temp_advice.append("Your temperature are below normal.")
      temp_advice.append("Your can...")
      temp_advice.append("1. Remove and replace any wet clothing and make sure their head is covered.")
      temp_advice.append("2. Try to protect the casualty from the ground.")
      temp_advice.append("3. If the casualty is fully alert, offer them warm drinks and high energy food such as chocolate.")
      temp_advice.append("4. Monitor their breathing, level of response and temperature while waiting for help to arrive.")

    elif temp >35 and temp <=37.5:
      temp_message = "Normal"
      temp_advice.append("Your temperature are Normal.")
      temp_advice.append("Keep going!")
    elif temp >37.5:
      temp_message = "Fever"
      temp_advice.append("Your temperature are above normal.")
      temp_advice.append("Your can...")
      temp_advice.append("1. Get lots of rest.")
      temp_advice.append("2. Drink plenty of fluids (water is best) to avoid dehydration – drink enough so your pee is light yellow and clear.")
      temp_advice.append("3. Take paracetamol or ibuprofen if you feel uncomfortable.")
      temp_advice.append("4. Stay at home and avoid contact with other people until you do not have a high temperature.")
    else:
      temp_message = "error"
    # =======================
    if HB == 0 :
      HB_message = "Heartbeat Not Yet Upload"
      HB_advice.append("You have not upload this data.")
    elif HB < 60 :
      HB_message = "Bradycardia"
      HB_advice.append("Your heartbeat below normal.")
      HB_advice.append("You can...")
      HB_advice.append("1. Eat a heart-healthy diet that includes vegetables, fruits, nuts, beans, lean meat, fish, and whole grains. Limit alcohol, sodium, and sugar.")
      HB_advice.append("2. Stay at a healthy weight. Lose weight if you need to.")
      HB_advice.append("3. Do not smoke.")
      HB_advice.append("4. Manage other health problems such as high cholesterol, and diabetes.")

    elif HB >=60 and HB <=100:
      HB_message = "Normal"
      HB_advice.append("Your heartbeat are Normal.")
      HB_advice.append("Keep going!")
    elif HB >100:
      HB_message = "Tachycardia"
      HB_advice.append("Your heartbeat above normal.")
      HB_advice.append("You can...")
      HB_advice.append("1. Cutting down on the amount of caffeine or alcohol you drink.")
      HB_advice.append("2. Stopping or cutting back on smoking.")
      HB_advice.append("3. Making sure you get enough rest.")
    else:
      HB_message = "error"
    # =======================
    if BP_sys==0 and BP_dia==0 :
      BP_message = "Blood Pressure Not Yet Upload"
      BP_advice.append("You have not upload this data.")
    elif BP_sys < 120 and BP_dia <80 :
      BP_message = "Normal"
      BP_advice.append("Your blood pressure are Normal.")
      BP_advice.append("Keep going!")
    elif (BP_sys >=120 and BP_sys <140) and (BP_dia >= 80 and BP_dia < 90):
      BP_message = "Prehypertension"
      BP_advice.append("Your blood pressure are at risk.")
      BP_advice.append("You can...")
      BP_advice.append("1. Lose weight if you are overweight.")
      BP_advice.append("2. Exercise regularly.")
      BP_advice.append("3. Eat plenty of fruits, vegetables, whole grains, fish, and low-fat dairy.")
      BP_advice.append("4. Cut back on dietary salt/sodium.")

    elif BP_sys >= 140 and BP_dia >=90:
      BP_message = "Hypertension"
      BP_advice.append("Your blood pressure are high.")
      BP_advice.append("You can...")
      BP_advice.append("1. Lose weight if you are overweight.")
      BP_advice.append("2. Exercise regularly.")
      BP_advice.append("3. Eat plenty of fruits, vegetables, whole grains, fish, and low-fat dairy.")
      BP_advice.append("4. Cut back on dietary salt/sodium.")
    else:
      BP_message = "error"
    # =======================
    if Spo2 == 0 :
      Spo2_message = "Blood Oxygen Not Yet Upload"
      Spo2_advice.append("You have not upload this data.")
    elif Spo2 < 80 :
      Spo2_message = "Hypoxemia"
      Spo2_advice.append("Your heartbeat below normal .")
      Spo2_advice.append("You can...")
      Spo2_advice.append("1. Inhalers with bronchodilators or steroids to help people with lung disease like COPD.")
      Spo2_advice.append("2. Medications that help to get rid of excess fluid in your lungs.")
      Spo2_advice.append("3.  Continuous positive airways pressure mask (CPAP) to treat sleep apnea.")
    elif Spo2 >=80 and Spo2 <=100:
      Spo2_message = "Normal "
      Spo2_advice.append("Your heartbeat are Normal.")
      Spo2_advice.append("Keep going!")
    elif Spo2 >100:
      Spo2_message = "High"
      Spo2_advice.append("Your heartbeat above normal.")
      Spo2_advice.append("You can...")
      Spo2_advice.append("1. Lie down in the prone position")
      Spo2_advice.append("2. Include more antioxidants in your diet.")
      Spo2_advice.append("3. Practice slow and deep breathing.")
    else:
      Spo2_message = "error"
    
    return render(request = request,
                  template_name='main/report.html',
                  context = {
                    'healthDatas':healthDatas,
                    'newestData' : newestData,
                    'temp_message' : temp_message,
                    'HB_message' : HB_message,
                    'BP_message' : BP_message,
                    'Spo2_message' : Spo2_message,
                    'temp_advice' : temp_advice,
                    'HB_advice' : HB_advice,
                    'BP_advice' : BP_advice,
                    'Spo2_advice' : Spo2_advice,
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




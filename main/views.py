from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models.expressions import F

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
    return render(request = request,
                  template_name='main/data.html',
                  context = {
                    'healthDatas':healthDatas,
                  })


# ===============================================================================================

def testpage(request):
    healthDatas = HealthData.objects.all()
    return render(request = request,
                  template_name='main/test.html',
                  context = {
                    'healthDatas':healthDatas,
                  })




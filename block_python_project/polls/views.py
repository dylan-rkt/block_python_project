from django.shortcuts import render, redirect
from polls.forms import BlockForm
from polls.block_ml import *

def accueil(request):
    return render(request,
                  'polls/accueil.html')

def parametersForm(request):
    form = BlockForm()
    return render(request,
                  'polls/parametersForm.html',
                  {'form': form})

def result(request):
    if request.method != 'POST':
        return redirect('parametersForm')
    form = BlockForm(request.POST)
    if not form.is_valid():
        return redirect('parametersForm')
    y_value = target(request)
    return render(request,
                  'polls/result.html',
                  {'values': y_value})



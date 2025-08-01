from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms


class TaskForm(forms.Form):
    task = forms.CharField(label='Task', max_length=100)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session['tasks'] = []
    return render(request, 'tasks/index.html', {'tasks': request.session['tasks']})

def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['tasks']+=[task]  # Add the new task to the list
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'tasks/add.html', {'form': form})
        
    return render(request, 'tasks/add.html', {'form': TaskForm()})
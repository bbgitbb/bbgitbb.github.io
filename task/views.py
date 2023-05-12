
from django.shortcuts import render
from django import forms


class AddTaskForm(forms.Form):
    task = forms.CharField(label="task")
    importance = forms.IntegerField(label="importance")



tasks: list[str] = [
    "add cat",
    "add dog"
]

def index(request):
    return render(request, 'task/index.html', {
        'tasks': tasks
    })

def add_task(request):
    return render(request, 'task/add_task.html', {
        'tasks': tasks,
        "form": AddTaskForm()
    })





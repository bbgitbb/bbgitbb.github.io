from typing import Callable, Iterable
from django.shortcuts import render



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
        'tasks': tasks
    })





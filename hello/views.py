from django.http import HttpResponse
from django.shortcuts import render
import time


def greet(request, name: str):
    return render(request, "hello/index.html", {
        "name": name
    })


def cum(request):
    return HttpResponse("cummed")








from django.shortcuts import render
from time import localtime

def index(request):
    _, month, day, *_ = localtime()
    return render(request, "newyear/index.html", {
        "is_newyear": month == 1 and day == 1
    })

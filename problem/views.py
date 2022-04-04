from django.shortcuts import render
from .models import *

# Create your views here.

def problems(request):
    problems = Problem.objects.all()[:10]
    context = {'problems': problems}
    return render(request, "index.html", context)
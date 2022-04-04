from django.shortcuts import render

# Create your views here.

def problems(request):
    return render(request, "index.html")
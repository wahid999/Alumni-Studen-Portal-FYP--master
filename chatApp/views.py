from django.shortcuts import render

def index(request):
    return render(request,'proj/build/index.html')
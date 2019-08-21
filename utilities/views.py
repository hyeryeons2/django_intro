from django.shortcuts import render

# Create your views here.

def index(request):         
    return render(request, 'utilities/index.html')

def image(request):
    return render(request, 'utilities/image.html')
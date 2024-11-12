from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def insert(request):
    return render(request, 'insert.html')


from django.shortcuts import render, redirect
from students.models import Student

# Create your views here.
def index(request):
    return render(request, 'index.html')

def insert(request):
    return render(request, 'insert.html')


def insert_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        phone = request.POST['phone']
        image = request.FILES['image']

        student = Student(name=name, email=email, age=age, phone=phone, image=image)
        student.save()
        return redirect('/')

    return render(request, 'insert.html')

def view_data(request):
    student = Student.objects.all()
    return render(request, 'viewdata.html', {"students": student})


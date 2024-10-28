from django.shortcuts import render, redirect
from .models import Person
from django.http import HttpResponse

# Create your views here.
def submit_person(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']

        person = Person(name=name,email=email,age=age)

        person.save()

        return redirect('success')
    
    return render(request, 'index.html')

def success_view(request):
    all_users = Person.objects.all()
    return render(request, 'success.html', {'all_users': all_users})

def home(request):
    return HttpResponse("This is cat 2")
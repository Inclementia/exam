from django.shortcuts import render
import random
from mainapp.models import Students


def index(request):
    name = ['Ложкина', "Обухов", "Достовалов", "Карпор", "Зырянов", "Пухов", "Теплов", "Газиев", "Курбонова",
            "Велижанина"]
    random_name = random.choice(name)
    context = {
        'name': random_name,
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


def student(request):
    students = Students.objects.all()
    context = {
        'students': students,
        'page_title': 'список'
    }
    return render(request, 'mainapp/student.html', context)

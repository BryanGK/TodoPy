from django.shortcuts import render
from . models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html',
                  {'todos': todos})


def create(request):
    return render(request, 'create.html')


def edit(request):
    return render(request, 'edit.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo.models import Todo

def list(request):
    lists = Todo.objects.all()
    return render(request, 'lists/home.html', {'lists':lists})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
# Create your views here.
def add(request):
    if request.method == "POST":
        print("You clicked add")
        head = request.POST['title']
        body = request.POST['body']
        reminder = Todo(head=head, body=body)
        reminder.save()
        return redirect('/')

def delete(request, list_id):
    if request.method == "POST":
        print("You clicked delete")
        reminder = Todo.objects.filter(id=list_id)
        reminder.delete()
        return redirect('/')

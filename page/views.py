from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.http import HttpResponseRedirect
# Create your views here.
def todoappView(request):
    all_todo_items = Post.objects.all()
    return render(request, 'home.html', {'all_items':all_todo_items})

def addTodoView(request):
    a = request.POST['body']
    new_item = Post(body=a)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    y = Post.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect("/todoapp/")


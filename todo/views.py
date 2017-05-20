import datetime

from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import generic
from django.views.generic import CreateView

from accounts.views import login_view
from todo.forms import TodoForm
from todo.models import ToDo


def IndexView(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        return redirect('accounts:login')
    all_todo = ToDo.objects.filter(Q(user__username=user.username),Q(publish=True))
    return render(request, "index.html", {"all_todo":all_todo,"user":user})


def DetailToDo(request,id):
    if not request.user.is_authenticated():
        return redirect('accounts:login')
    todo = get_object_or_404(ToDo, id=id)

    return render(request, "detail.html", {"todo":todo})

def AddTodo(request):
    if not request.user.is_authenticated():
        return redirect('accounts:login')
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return IndexView(request)
    else:
        form = TodoForm()
    return render(request, 'addtodo.html', {'form': form})

def SearchTodo(request):
    return redirect('todo:index')

def TodoDone(request, id):
    if not request.user.is_authenticated():
        return redirect('accounts:login')
    todo = get_object_or_404(ToDo, id=id)
    if(todo.done == False):
        todo.done = True
        todo.publish = False
    else:
        todo.done = False
        todo.publish = True
    todo.save()
    return redirect('todo:detail', id = todo.id)

def ProfileView(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        return redirect('accounts:login')
    all_todo = ToDo.objects.filter(user__username=user.username)
    return render(request, "profile.html", {"all_todo":all_todo, "user":user})


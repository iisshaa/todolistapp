from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm, UpdateTaskForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')

    else:
        f = UserCreationForm()

    return render(request, 'registration/register.html', {'form': f})


@login_required()
def home(request):
    todos = Task.objects.filter(user=request.user)
    count_todos = todos.count()
    completed_todo = Task.objects.filter(complete=True)
    count_completed_todo = completed_todo.count()
    count_uncompleted_todo = count_todos - count_completed_todo
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    context = {
        'todos': todos,
        'form': form,
        'count_todos': count_todos,
        'count_completed_todo': count_completed_todo,
        'count_uncompleted_todo': count_uncompleted_todo

    }
    return render(request, 'todo/home.html', context)


def update(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateTaskForm(instance=task)
    context = {
        'form': form
    }
    return render(request, 'todo/update.html', context)


def delete(request, pk):
    todo = Task.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('/')
    return render(request, 'todo/delete.html')

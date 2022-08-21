from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoCreatedForm, TodoUpdateForm


def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', context={'todos': all})


def sey_hello(request):
    person = {'name': 'Ali..............'}
    return render(request, 'hello.html', context=person)


def details(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'details.html', {'todo': todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'Todo deleted successfully', extra_tags='success')
    return redirect('home')


def create(request):

    if request.method == 'POST':
        form = TodoCreatedForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], content=cd['content'], created=cd['created'])
            messages.success(request, 'Form success added', 'success')
            return redirect('home')
    else:
        form = TodoCreatedForm()
    return render(request, 'create.html', {'form': form})


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'your todo updated successfully', 'success')
            return redirect('details', todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
        return render(request, 'update.html', {'form': form})

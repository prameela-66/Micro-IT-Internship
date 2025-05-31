from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.utils import timezone

def index(request):
    todos = Todo.objects.filter(completed=False).order_by('-id')
    completed_todos = Todo.objects.filter(completed=True).order_by('-completed_on')
    show_completed = request.GET.get('show_completed') == 'true'

    context = {
        'todos': todos,
        'completed_todos': completed_todos,
        'show_completed': show_completed,
    }
    return render(request, 'todoapp/index.html', context)

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            Todo.objects.create(title=title, description=description)
    return redirect('/')

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('/')

def complete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.completed = True
    todo.completed_on = timezone.now()
    todo.save()
    return redirect('/')

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            todo.title = title
            todo.description = description
            todo.save()
            return redirect('/')
    context = {'todo': todo}
    return render(request, 'todoapp/edit.html', context)

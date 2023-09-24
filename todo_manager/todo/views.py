from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        name = request.POST['name']  # Use square brackets here
        description = request.POST['description']
        due_date = request.POST['due_date']
        Task.objects.create(name=name, description=description, due_date=due_date)  # Include the 'name' attribute
        return redirect('task_list')
    return render(request, 'todo/add_task.html')

def mark_completed(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('task_list')

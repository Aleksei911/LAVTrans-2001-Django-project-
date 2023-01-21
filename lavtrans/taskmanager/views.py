from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def main(request):
    tasks = Task.objects.all().order_by('complete_to')
    return render(request, 'taskmanager/main.html', {'title': 'Задачи', 'tasks': tasks})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = 'Некорректно внесены данные'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'taskmanager/create.html', context)

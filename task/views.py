from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Task
from . forms import TaskForm



def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'tasks':tasks,
        'form':form
        }
    return render(request,'task/index.html',context)

def update_task(request,id):
    tasks = Task.objects.get(pk=id)
    form = TaskForm(instance=tasks)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=tasks)
        form.save()
        return redirect('/')
    return render(request,'task/task_update.html',{'form':form})

def delete_task(request,id):
    item = Task.objects.get(pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request,'task/task_delete.html',{'item':item})
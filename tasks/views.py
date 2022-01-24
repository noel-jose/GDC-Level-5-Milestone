# Add your Views Here
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from tasks.models import Task


def task_view(request):
    search_value = request.GET.get("search")
    tasks = Task.objects.filter(deleted=False)
    if search_value:
        tasks = tasks.filter(title__icontains=search_value)
    return render(request, "task.html", {"tasks": tasks})


def add_task_view(request):
    task_title = request.GET.get("task")
    task_object = Task(title=task_title)
    task_object.save()
    return HttpResponseRedirect("/tasks/")


def delete_task_view(request, task_id):
    Task.objects.filter(id=task_id).update(deleted=True)
    return HttpResponseRedirect("/tasks/")


def complete_task_view(request, index):
    completed_task = tasks.pop(index - 1)
    completed.append(completed_task)
    return HttpResponseRedirect("/tasks/")


def completed_task_view(request):
    return render(request, "completed.html", {"tasks": completed})


def all_tasks_view(request):
    return render(request, "all.html", {"tasks": tasks, "completed": completed})

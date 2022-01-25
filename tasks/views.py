# Add your Views Here
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from tasks.models import Task


def task_view(request):
    search_value = request.GET.get("search")
    tasks = Task.objects.filter(deleted=False, completed=False)
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


def complete_task_view(request, task_id):
    completed_task = Task.objects.filter(id=task_id)
    completed_task.update(completed=True)
    return HttpResponseRedirect("/tasks/")


def completed_task_view(request):
    completed = Task.objects.filter(completed=True, deleted=False)
    return render(request, "completed.html", {"tasks": completed})


def all_tasks_view(request):
    tasks = Task.objects.filter(deleted=False)
    pending_tasks = tasks.filter(completed=False)
    completed_tasks = tasks.filter(completed=True)
    return render(
        request, "all.html", {"tasks": pending_tasks, "completed": completed_tasks}
    )

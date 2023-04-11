from django.shortcuts import render

from sailors_app.models import Task


def index(request):
    num_tasks = Task.objects.count()

    context = {
        "num_tasks": num_tasks
    }

    return render(request, "base.html", context=context)

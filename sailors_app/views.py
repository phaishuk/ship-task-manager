from django.shortcuts import render
from django.views import generic

from sailors_app.models import Task, Sailor, Position


def index(request):
    num_tasks = Task.objects.count()
    num_sailors = Sailor.objects.count()
    num_positions = Position.objects.count()

    context = {
        "num_tasks": num_tasks,
        "num_sailors": num_sailors,
        "num_positions": num_positions,
    }

    return render(request, "sailors_app/index.html", context=context)


class SailorListView(generic.ListView):
    model = Sailor
    fields = "__all__"


class SailorDetailView(generic.DetailView):
    model = Sailor


class TaskListView(generic.ListView):
    model = Task
    fields = "__all__"


class TaskDetailView(generic.DetailView):
    model = Task


class PositionListView(generic.ListView):
    model = Position
    fields = "__all__"


class PositionDetailView(generic.DetailView):
    model = Position

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from sailors_app.models import Task, Sailor, Position


@login_required
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


class SailorListView(LoginRequiredMixin, generic.ListView):
    model = Sailor


class SailorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Sailor


class SailorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Sailor
    fields = "__all__"
    success_url = reverse_lazy("sailors_app:sailor-list")


class SailorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Sailor
    fields = "__all__"
    success_url = reverse_lazy("sailors_app:sailor-list")


class SailorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Sailor
    success_url = reverse_lazy("sailors_app:sailor-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position

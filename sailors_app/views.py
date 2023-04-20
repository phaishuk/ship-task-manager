from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from sailors_app.forms import (
    SailorCreationForm, SailorUpdateForm, TaskForm, SearchSailors,
    SearchPositions, SearchTasks
)
from sailors_app.models import Task, Sailor, Position


@login_required
def index(request):
    num_tasks = Task.objects.count()
    num_sailors = Sailor.objects.count()
    num_positions = Position.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_tasks": num_tasks,
        "num_sailors": num_sailors,
        "num_positions": num_positions,
        "num_visits": num_visits + 1,
    }

    return render(request, "sailors_app/index.html", context=context)


@login_required
def toggle_assign_to_task(request, pk):
    sailor = Sailor.objects.get(id=request.user.id)
    if (
        Task.objects.get(id=pk) in sailor.tasks.all()
    ):
        sailor.tasks.remove(pk)
    else:
        sailor.tasks.add(pk)
    return HttpResponseRedirect(reverse_lazy(
        "sailors_app:task-detail", args=[pk])
    )


@login_required
def user_tasks(request):
    sailor = Sailor.objects.get(id=request.user.id)
    tasks = sailor.tasks.all()
    context = {'tasks': tasks}
    return render(request, 'sailors_app/user_tasks.html', context)


class SailorListView(LoginRequiredMixin, generic.ListView):
    model = Sailor
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SailorListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")
        context["first_name"] = SearchSailors(initial={
            "title": title
        })

        return context

    def get_queryset(self):
        queryset = Sailor.objects.select_related("position")
        first_name = self.request.GET.get("first_name")

        if first_name:
            return queryset.filter(first_name__icontains=first_name)
        return queryset


class SailorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Sailor
    queryset = Sailor.objects.prefetch_related("tasks__assignees")


class SailorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Sailor
    form_class = SailorCreationForm
    success_url = reverse_lazy("sailors_app:sailor-list")


class SailorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Sailor
    form_class = SailorUpdateForm
    success_url = reverse_lazy("sailors_app:sailor-list")


class SailorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Sailor
    success_url = reverse_lazy("sailors_app:sailor-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")
        context["name"] = SearchTasks(initial={
            "title": title
        })

        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        name = self.request.GET.get("name")

        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("sailors_app:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("sailors_app:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("sailors_app:task-list")


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")
        context["name"] = SearchPositions(initial={
            "title": title
        })

        return context

    def get_queryset(self):
        queryset = Position.objects.all()
        name = self.request.GET.get("name")

        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("sailors_app:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("sailors_app:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("sailors_app:position-list")

from django.contrib import admin
from django.urls import path

from sailors_app.views import (
    index, user_tasks,
    TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView,
    TaskDeleteView,
    PositionListView, PositionDetailView, PositionCreateView,
    PositionUpdateView, PositionDeleteView,
    SailorListView, SailorDetailView, SailorCreateView, SailorUpdateView,
    SailorDeleteView,
    toggle_assign_to_task,
)

app_name = "sailors_app"

urlpatterns = [
    path(
        "admin/",
        admin.site.urls
    ),
    path(
        "",
        index,
        name="index"
    ),
    path(
        "user_tasks/",
        user_tasks,
        name="user_tasks"
    ),
    path(
        "sailors/",
        SailorListView.as_view(),
        name="sailor-list"
    ),
    path(
        "sailor/<int:pk>/",
        SailorDetailView.as_view(),
        name="sailor-detail"
    ),
    path(
        "sailor/create/",
        SailorCreateView.as_view(),
        name="sailor-create"
    ),
    path(
        "sailor/<int:pk>/update/",
        SailorUpdateView.as_view(),
        name="sailor-update"
    ),
    path(
        "sailor/<int:pk>/delete/",
        SailorDeleteView.as_view(),
        name="sailor-delete"
    ),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "task/<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail"
    ),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "task/<int:pk>/toggle-assign/",
        toggle_assign_to_task,
        name="toggle-task-assign",
    ),
    path(
        "positions/",
        PositionListView.as_view(),
        name="position-list"
    ),
    path(
        "position/<int:pk>/",
        PositionDetailView.as_view(),
        name="position-detail"
    ),
    path(
        "position/create/",
        PositionCreateView.as_view(),
        name="position-create"
    ),
    path(
        "position/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update"
    ),
    path(
        "position/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete"
    ),
]

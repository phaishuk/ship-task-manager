from django.contrib import admin
from django.urls import path

from sailors_app.views import (
    index,
    TaskListView,
    TaskDetailView,
    PositionListView,
    SailorListView,
    SailorDetailView,
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
        "sailor/",
        SailorListView.as_view(),
        name="sailor-list"
    ),
    path(
        "sailor/<int:pk>",
        SailorDetailView.as_view(),
        name="sailor-detail"
    ),
    path(
        "task/",
        TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "task/<int:pk>",
        TaskDetailView.as_view(),
        name="task-detail"
    ),
    path(
        "position/",
        PositionListView.as_view(),
        name="position-list"
    ),
]

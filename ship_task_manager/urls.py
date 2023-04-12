"""
URL configuration for ship_task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from sailors_app.views import (
    index,
    TaskListView,
    TaskDetailView,
    PositionListView,
    PositionDetailView,
    SailorListView,
    SailorDetailView,
)

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

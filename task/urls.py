from django.urls import path

from .views import CreateLabelView, CreateTaskView, LabelListView, UpdateLabelView, UpdateTaskView, MoveTaskView, DeleteTaskView, DeleteLabelView

urlpatterns = [
    path(
        "create-label/",
        CreateLabelView.as_view(),
    ),
    path(
        "create-task/",
        CreateTaskView.as_view(),
    ),
    path(
        "labels/",
        LabelListView.as_view(),
    ),
    path(
        "label/<int:pk>/",
        UpdateLabelView.as_view(),
    ),
    path(
        "task/<int:pk>/",
        UpdateTaskView.as_view(),
    ),
    path(
    "task/<int:pk>/move/",
    MoveTaskView.as_view(),
    ),
    path(
    "task/<int:pk>/delete/",
    DeleteTaskView.as_view(),
    ),

path(
    "label/<int:pk>/delete/",
    DeleteLabelView.as_view(),
    ),
]
from django.urls import path

from .views import TaskViewSet

urlpatterns = [
    path(
        "todo/tasks/",
        TaskViewSet.as_view({"get": "list", "post": "create"}),
        name="todo-tasks",
    ),
    path(
        "todo/tasks/<int:pk>/",
        TaskViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="todo-tasks-pk",
    ),
]

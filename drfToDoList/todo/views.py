from rest_framework import viewsets

from .models import Task, Log
from .serializers import TaskSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.order_by("id")
    serializer_class = TaskSerializer


    # 使用 JWT 驗證
    authentication_classes = [JWTAuthentication]
    # 只允許通過驗證的使用者存取
    permission_classes = [IsAuthenticated]
  
    def create(self, request, *args, **kwargs):
        if self.queryset.filter(title=request.data.get("title")):
            return Response({'title_name':["工作已存在"]}, status=status.HTTP_400_BAD_REQUEST)
        title = request.data.get("title")
        description = request.data.get("description", "")
        task_serializer = self.get_serializer(data={"title": title, "description": description})
        task_serializer.is_valid(raise_exception=True)
        task = task_serializer.save()
        Log.objects.create(action=1, task=task)
        return Response(task_serializer.data, status=status.HTTP_201_CREATED)


    def list(self, request, *args, **kwargs):
    # 過濾出建立時間早於指定時間的任務
    #    queryset = self.get_queryset().filter(created_at__lt=timezone.datetime(2024, 5, 6, 2,4 ))
    # 過濾出建立時間晚於指定時間的任務
       queryset = self.get_queryset().filter(created_at__gt=timezone.datetime(2024, 5, 6, 2,4 ))
    # # 過濾指定時間的任務    
    #    queryset = self.get_queryset().filter(created_at__range=(timezone.datetime(2024, 5, 6, 1, 41),timezone.datetime(2024, 5, 7, 2, 42)))
       
       serializer = TaskSerializer(queryset, many=True)
       return Response(serializer.data)
       
    
    def retrieve(self, request, *args, **kwargs):
        task = self.get_object()
        task_serializer = TaskSerializer(task)
        Log.create_log(action=4, task=task)
        return Response(task_serializer.data, status=status.HTTP_202_ACCEPTED)

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.title != request.data.get("title") and self.queryset.filter(title=request.data.get("title")).exists():
            return Response({'title_name':["工作不存在"]}, status=status.HTTP_400_BAD_REQUEST)
        title = request.data.get("title")
        description = request.data.get("description", "")
        task_serializer = self.get_serializer(task, data={"title": title, "description": description}, partial=True)
        task_serializer.is_valid(raise_exception=True)
        task = task_serializer.save()
        Log.objects.create(action=3, task=task)
        return Response(task_serializer.data, status=status.HTTP_205_RESET_CONTENT)

    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        Log.create_log(action=2, task=task)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

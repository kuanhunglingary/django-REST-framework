from django.contrib import admin
from .models import Task, Log


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','created_at',]
    search_fields = ['title',]


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['action', 'task']

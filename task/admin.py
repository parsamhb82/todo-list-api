from django.contrib import admin
from .models import Task, Label

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ...
@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    ...

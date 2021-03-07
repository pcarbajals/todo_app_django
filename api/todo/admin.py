from django.contrib import admin
from .models import Task

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'due_date')

admin.site.register(Task, TodoAdmin)

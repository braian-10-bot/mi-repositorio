from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created_at', 'updated_at')  # Asegúrate de que estos campos existen en el modelo

admin.site.register(Task, TaskAdmin)
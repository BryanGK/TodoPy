from django.contrib import admin
from . models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('todo', 'is_completed', 'due_date')


admin.site.register(Todo, TodoAdmin)

from django.contrib import admin
from .models import Todo
# Register your models here.

# admin.site.register(Todo)

# @admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
   list_display = ['title', 'description','status']
   list_per_page = 5
   list_filter = ['status']      # Todo.objects.filter(status=True/False)
   search_fields = ("title",)
   list_editable = ('status',)

admin.site.register(Todo, TodoAdmin)
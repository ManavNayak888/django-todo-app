from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','user','title', 'complete', 'created')
    list_filter = ('complete', 'created')
    search_fields = ('title', 'decription', 'user__username')

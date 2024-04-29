from django.contrib import admin
from .models import BugReport, FeatureRequest
# Register your models here.

class BugInline(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True


inlines = [BugInline]
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'priority', 'project')
    fieldsets = [
        ('Проект', {'fields': ['project']}),
        ('Задача', {'fields': ['task']}),
        ('Название', {'fields': ['title']}),
        ('Описание', {'fields': ['description']}),
        ('Статус', {'fields': ['status']}),
        ('Приоритет', {'fields': ['priority']}),
    ]
    ordering = ('created_at',)
    date_hierarchy = 'created_at'



@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'priority', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    fieldsets = [
        ('Проект', {'fields': ['project']}),
        ('Задача', {'fields': ['task']}),
        ('Название', {'fields': ['title']}),
        ('Описание', {'fields': ['description']}),
        ('Статус', {'fields': ['status']}),
        ('Приоритет', {'fields': ['priority']}),
    ]
    readonly_fields = ('created_at', 'updated_at')
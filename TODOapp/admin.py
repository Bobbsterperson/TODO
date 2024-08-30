from django.contrib import admin
from .models import TODO

@admin.action(description='DONE')
def mark_as_completed(modeladmin, request, queryset):
    for todo in queryset:
        todo.completed = True
        todo.save()

@admin.action(description='DELETE')
def delete_selected(modeladmin, request, queryset):
    queryset.delete()

class TODOAdmin(admin.ModelAdmin):
    list_display = ('TODO',)
    actions = [mark_as_completed, delete_selected]

admin.site.register(TODO, TODOAdmin)

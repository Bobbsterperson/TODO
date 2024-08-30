from django.contrib import admin
from .models import TODO, Done

@admin.action(description='DONE')
def mark_as_done(modeladmin, request, queryset):
    for todo in queryset:
        Done.objects.create(original_todo=todo.TODO, deleted=True)
        todo.delete()

@admin.action(description='Delete Selected')
def delete_selected(modeladmin, request, queryset):
    for todo in queryset:
        Done.objects.create(original_todo=todo.TODO, deleted=True)
        todo.delete()

class TODOAdmin(admin.ModelAdmin):
    list_display = ('TODO', 'created_at')
    actions = [mark_as_done, delete_selected]

admin.site.register(TODO, TODOAdmin)

class DoneTODOAdmin(admin.ModelAdmin):
    list_display = ('original_todo', 'deleted', 'timestamp')
    readonly_fields = ('timestamp',)

admin.site.register(Done, DoneTODOAdmin)

from django.contrib import admin
from .models import TODO


admin.site.register(TODO)
# class TODOAdmin(admin.ModelAdmin):
#     list_display = ('TODO', 'created_at', 'category', 'completed')  # Display the completed status
#     list_filter = ('completed', 'category', 'created_at')  # Add filters for better navigation
#     search_fields = ('TODO', 'category')  # Allow searching by task description and category
#     list_editable = ('completed', 'category')  # Allow inline editing of completed status and category
#     ordering = ('-created_at',)  # Order tasks by creation date, newest first


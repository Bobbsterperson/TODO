from django.contrib import admin
from .models import TODO


class TODOAdmin(admin.ModelAdmin):
    list_display = ('TODO', 'created_at', 'category')
    
admin.site.register(TODO, TODOAdmin)


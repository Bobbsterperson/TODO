from django.contrib import admin
from .models import TODO, DONE

admin.site.register(TODO)
admin.site.register(DONE)
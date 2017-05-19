from django.contrib import admin

# Register your models here.
from todo.models import ToDo

admin.site.register(ToDo)
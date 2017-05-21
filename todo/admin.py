from django.contrib import admin
from django.db import models

from .models import ToDo
from markdownx.widgets import AdminMarkdownxWidget

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    list_display = ["title", "user"]
    list_filter = ["user"]
    search_fields = ["title", "user"]

    class Meta:
        model = ToDo

admin.site.register(ToDo, MyModelAdmin)
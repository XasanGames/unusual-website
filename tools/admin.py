# tools/admin.py
from django.contrib import admin
from .models import Snippet

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "code")

from django.contrib import admin
from .models import Poll, Option, Vote

# Register your models here
@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ['question', 'created_by', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['question']

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['text', 'poll', 'created_at']
    list_filter = ['poll']
    search_fields = ['text']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['option', 'user', 'voted_at']
    list_filter = ['voted_at', 'option__poll']
    search_fields = ['option__text']



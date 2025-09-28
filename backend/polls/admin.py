from django.contrib import admin
from .models import Poll, Choice, Vote

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ['question', 'created_by', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['question']

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'poll', 'votes']
    list_filter = ['poll']
    search_fields = ['choice_text']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['poll', 'choice', 'voter', 'voted_at']
    list_filter = ['voted_at', 'poll']
    search_fields = ['voter__username']


from django.urls import path
from . import views

urlpatterns = [
    path('polls/', views.poll_list, name='poll-list'),           # List all polls
    path('polls/<int:poll_id>/', views.poll_detail, name='poll-detail'),  # Single poll
    path('polls/<int:poll_id>/vote/', views.vote, name='vote'),           # Vote
    path('polls/<int:poll_id>/results/', views.poll_results, name='poll-results'),  # Results
]
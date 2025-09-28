from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('polls/', views.poll_list, name='poll-list'),
    path('polls/<int:poll_id>/', views.poll_detail, name='poll-detail'),
    path('polls/<int:poll_id>/vote/', views.vote, name='vote'),
    path('polls/<int:poll_id>/results/', views.poll_results, name='poll-results'),
    
    # Authentication
    path('auth/token/', obtain_auth_token, name='api_token_auth'),
    path('auth/', include('rest_framework.urls')),
]
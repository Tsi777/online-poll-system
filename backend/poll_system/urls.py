from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def poll_list(request):
    return JsonResponse({'message': 'Poll list working!', 'status': 'success'})

def poll_detail(request, poll_id):
    return JsonResponse({'message': f'Poll {poll_id} details working!', 'poll_id': poll_id})

@csrf_exempt
def vote(request, poll_id):
    if request.method == 'POST':
        return JsonResponse({'message': f'Vote for poll {poll_id} recorded!', 'poll_id': poll_id})
    return JsonResponse({'error': 'POST method required'}, status=405)

def poll_results(request, poll_id):
    return JsonResponse({'message': f'Results for poll {poll_id} working!', 'poll_id': poll_id})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/polls/', poll_list),
    path('api/polls/<int:poll_id>/', poll_detail),
    path('api/polls/<int:poll_id>/vote/', vote),
    path('api/polls/<int:poll_id>/results/', poll_results),
]

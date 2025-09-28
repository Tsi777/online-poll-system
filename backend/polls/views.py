from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Poll, Option, Vote

def poll_list(request):
    polls = Poll.objects.all()
    polls_data = []
    for poll in polls:
        options = Option.objects.filter(poll=poll)
        poll_data = {
            'id': poll.id,
            'question': poll.question,
            'options': [{'id': opt.id, 'text': opt.text} for opt in options]
        }
        polls_data.append(poll_data)
    return JsonResponse({'polls': polls_data})

def poll_detail(request, poll_id):
    try:
        poll = Poll.objects.get(id=poll_id)
        options = Option.objects.filter(poll=poll)
        return JsonResponse({
            'id': poll.id,
            'question': poll.question,
            'options': [{'id': opt.id, 'text': opt.text} for opt in options]
        })
    except Poll.DoesNotExist:
        return JsonResponse({'error': 'Poll not found'}, status=404)

@csrf_exempt
def vote(request, poll_id):
    if request.method == 'POST':
        try:
            option_id = request.POST.get('option_id')
            if not option_id:
                return JsonResponse({'error': 'option_id is required'}, status=400)
            
            # Create vote
            option = Option.objects.get(id=option_id)
            vote = Vote.objects.create(option=option)
            
            return JsonResponse({
                'message': 'Vote recorded successfully!',
                'vote_id': vote.id,
                'option': option.text
            })
        except Option.DoesNotExist:
            return JsonResponse({'error': 'Invalid option_id'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'POST method required'}, status=405)

def poll_results(request, poll_id):
    try:
        poll = Poll.objects.get(id=poll_id)
        options = Option.objects.filter(poll=poll)
        
        results = []
        total_votes = 0
        
        for option in options:
            vote_count = Vote.objects.filter(option=option).count()
            total_votes += vote_count
            results.append({
                'option_id': option.id,
                'option_text': option.text,
                'votes': vote_count
            })
        
        # Calculate percentages
        for result in results:
            if total_votes > 0:
                result['percentage'] = round((result['votes'] / total_votes) * 100, 2)
            else:
                result['percentage'] = 0.0
        
        return JsonResponse({
            'poll_id': poll_id,
            'poll_question': poll.question,
            'total_votes': total_votes,
            'results': results
        })
    except Poll.DoesNotExist:
        return JsonResponse({'error': 'Poll not found'}, status=404)
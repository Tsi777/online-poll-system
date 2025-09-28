from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Poll, Choice, Vote  # Changed Option to Choice

def poll_list(request):
    polls = Poll.objects.all()
    polls_data = []
    for poll in polls:
        options = Choice.objects.filter(poll=poll)  # Changed Option to Choice
        poll_data = {
            'id': poll.id,
            'question': poll.question,
            'options': [{'id': opt.id, 'text': opt.choice_text} for opt in options]  # Changed opt.text to opt.choice_text
        }
        polls_data.append(poll_data)
    return JsonResponse({'polls': polls_data})

def poll_detail(request, poll_id):
    try:
        poll = Poll.objects.get(id=poll_id)
        options = Choice.objects.filter(poll=poll)  # Changed Option to Choice
        return JsonResponse({
            'id': poll.id,
            'question': poll.question,
            'options': [{'id': opt.id, 'text': opt.choice_text} for opt in options]  # Changed opt.text to opt.choice_text
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
            option = Choice.objects.get(id=option_id)  # Changed Option to Choice
            vote = Vote.objects.create(choice=option)  # Changed option=option to choice=option
            
            return JsonResponse({
                'message': 'Vote recorded successfully!',
                'vote_id': vote.id,
                'option': option.choice_text  # Changed option.text to option.choice_text
            })
        except Choice.DoesNotExist:  # Changed Option to Choice
            return JsonResponse({'error': 'Invalid option_id'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'POST method required'}, status=405)

def poll_results(request, poll_id):
    try:
        poll = Poll.objects.get(id=poll_id)
        options = Choice.objects.filter(poll=poll)  # Changed Option to Choice
        
        results = []
        total_votes = 0
        
        for option in options:
            vote_count = Vote.objects.filter(choice=option).count()  # Changed option=option to choice=option
            total_votes += vote_count
            results.append({
                'option_id': option.id,
                'option_text': option.choice_text,  # Changed option.text to option.choice_text
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
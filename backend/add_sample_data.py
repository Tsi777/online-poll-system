import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poll_system.settings')
django.setup()

from polls.models import Poll, Option
from django.contrib.auth.models import User

def create_sample_polls():
    # Get the admin user
    admin_user = User.objects.get(username='admin')
    
   # questions with options
    polls_data = [
        {
            'question': 'What is your favorite programming language?',
            'options': ['Python', 'JavaScript', 'Ruby', 'Java']
        },
        {
            'question': 'What is your preferred database?',
            'options': ['MySQL', 'PostgreSQL', 'MongoDB', 'SQLite']
        },
        {
            'question': 'What is the biggest challenge you face during your time at ALX?',
            'options': [
                'The weekly pressure of deadlines and submissions',
                'Balancing the course with other personal responsibilities (work, classes)',
                'Lack of peer support',
                'A and B',
                'Other'
            ]
        },
        {
            'question': 'What is the best advice you would give to someone who is in the first week of the Prodev ALX program to successfully complete the course?',
            'options': [
                'Stay committed and learn through challenges. #WeDoHardThings',
                'The best thing about ALX is finding peers to share this journey with, so reach out on Discord or WhatsApp.',
                'Mentor support is available only on weekdays, so start early to seek guidance from mentors.',
                'Do not let AI replace you; use AI wisely in your journey.',
                'All of the above',
                'Other'
            ]
        },
        {
            'question': 'Choose one thing that has helped you the most during your time at ALX.',
            'options': [
                'Peer support',
                'The live build sessions',
                'Support from my mentors',
                'City Hub',
                'All of the above'
            ]
        },
        {
            'question': 'If you had the chance, to whom would you like to give a special thank you?',
            'options': [
                'Faith Okoth',
                'Irene Aragona',
                'Cole Baidoo',
                'All my mentors'
            ]
        },
        {
            'question': 'What is your preferred method of communication with peers?',
            'options': ['Discord', 'WhatsApp', 'Email', 'In-person meetings']
        },
        {
            'question': 'How do you feel about the pace of the Prodev ALX program?',
            'options': ['Too fast', 'Just right', 'Too slow', 'I don\'t have an opinion']
        },
        {
            'question': 'What resources do you find most useful for your learning?',
            'options': [
                'Online resources (tutorials, articles)',
                'Books',
                'Peer discussions',
                'Mentor sessions'
            ]
        },
        {
            'question': 'How often do you participate in study groups?',
            'options': ['Always', 'Often', 'Sometimes', 'Rarely', 'Never']
        },
        {
            'question': 'What topic would you like to learn more about in the future?',
            'options': [
                'Advanced algorithms',
                'Web development',
                'Data analysis',
                'Machine learning'
            ]
        },
    ]
    
    # Create polls and options
    for poll_data in polls_data:
        poll = Poll.objects.create(
            question=poll_data['question'],
            created_by=admin_user,
            is_active=True
        )
        
        for option_text in poll_data['options']:
            Option.objects.create(
                poll=poll,
                text=option_text
            )
        
        print(f'Created poll: {poll.question} with {len(poll_data["options"])} options')
    
    print(f'\nSuccessfully created {len(polls_data)} polls with options!')

if __name__ == '__main__':
    create_sample_polls()
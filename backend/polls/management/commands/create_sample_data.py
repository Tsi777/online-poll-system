from django.core.management.base import BaseCommand
from polls.models import Poll, Choice
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Create sample poll data"

    def handle(self, *args, **options):
        # Create a user if doesn't exist
        user, created = User.objects.get_or_create(
            username="admin",
            defaults={"email": "admin@example.com"}
        )
        
        if created:
            user.set_password("admin123")
            user.save()
            self.stdout.write(self.style.SUCCESS("Created admin user"))

        # Sample polls
        polls_data = [
            {
                "question": "What is your favorite programming language?",
                "choices": ["Python", "JavaScript", "Java", "C++", "Go"]
            },
            {
                "question": "Which web framework do you prefer?",
                "choices": ["Django", "Flask", "FastAPI", "Express.js", "Spring Boot"]
            },
        ]

        for poll_data in polls_data:
            poll, created = Poll.objects.get_or_create(
                question=poll_data["question"],
                defaults={"created_by": user}
            )
            
            if created:
                for choice_text in poll_data["choices"]:
                    Choice.objects.create(poll=poll, choice_text=choice_text)
                
                self.stdout.write(
                    self.style.SUCCESS(f'Created poll: "{poll.question}"')
                )

        self.stdout.write(self.style.SUCCESS("Sample data created successfully!"))

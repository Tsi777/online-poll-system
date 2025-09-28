from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Poll(models.Model):
    question = models.CharField(max_length=500)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['is_active', 'expires_at']),
            models.Index(fields=['created_at']),
        ]
        ordering = ['-created_at']
    
    @property
    def is_expired(self):
        if self.expires_at:
            return timezone.now() > self.expires_at
        return False
    
    def total_votes(self):
        return Vote.objects.filter(option__poll=self).count()
    
    def __str__(self):
        return self.question

class Option(models.Model):
    poll = models.ForeignKey(Poll, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['poll']),
        ]
    
    def vote_count(self):
        return self.vote_set.count()
    
    def __str__(self):
        return f"{self.poll.question} - {self.text}"

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)
    user_session = models.CharField(max_length=100, blank=True)  # For anonymous voting
    
    class Meta:
        unique_together = ['user', 'option']
        indexes = [
            models.Index(fields=['user', 'option']),
            models.Index(fields=['option']),
            models.Index(fields=['user_session']),
        ]
    
    def __str__(self):
        username = self.user.username if self.user else 'Anonymous'
        return f"{username} voted for {self.option.text}"

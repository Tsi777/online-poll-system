from rest_framework import serializers
from .models import Poll, Option, Vote
from django.utils import timezone

class OptionSerializer(serializers.ModelSerializer):
    vote_count = serializers.ReadOnlyField()
    
    class Meta:
        model = Option
        fields = ['id', 'text', 'vote_count']

class PollListSerializer(serializers.ModelSerializer):
    total_votes = serializers.ReadOnlyField()
    options_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Poll
        fields = ['id', 'question', 'created_at', 'total_votes', 'options_count', 'is_active']
    
    def get_options_count(self, obj):
        return obj.options.count()

class PollDetailSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    total_votes = serializers.ReadOnlyField()
    is_expired = serializers.ReadOnlyField()
    created_by = serializers.StringRelatedField()
    
    class Meta:
        model = Poll
        fields = ['id', 'question', 'created_by', 'created_at', 'expires_at', 
                 'is_active', 'is_expired', 'options', 'total_votes']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'option', 'voted_at']
        read_only_fields = ['voted_at']

class VoteCreateSerializer(serializers.Serializer):
    option_id = serializers.IntegerField()
    
    def validate_option_id(self, value):
        try:
            option = Option.objects.get(id=value)
            if not option.poll.is_active:
                raise serializers.ValidationError("This poll is not active.")
            if option.poll.is_expired:
                raise serializers.ValidationError("This poll has expired.")
            return value
        except Option.DoesNotExist:
            raise serializers.ValidationError("Invalid option ID.")
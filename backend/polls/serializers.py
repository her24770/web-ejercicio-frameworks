from rest_framework import serializers
from .models import Poll, Option


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ["id", "text", "votes"]


class PollSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    total_votes = serializers.SerializerMethodField()

    class Meta:
        model = Poll
        fields = ["id", "question", "created_at", "total_votes", "options"]

    def get_total_votes(self, obj):
        return obj.total_votes

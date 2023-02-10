from rest_framework import serializers
from .models import MbtiQuestion, Mbti

class MbtiQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MbtiQuestion
        fields = ('title', 'body', 'answer',)

class MbtiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mbti
        fields = ('name', 'description',)
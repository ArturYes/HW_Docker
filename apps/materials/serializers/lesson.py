from rest_framework import serializers

from apps.materials.models import Lesson
from apps.materials.validators import UrlLessonsValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlLessonsValidator(field='url')]

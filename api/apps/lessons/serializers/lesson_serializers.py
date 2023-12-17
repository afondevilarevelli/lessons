from rest_framework import serializers
from apps.lessons.models.lesson import Lesson
from apps.students.serializers import StudentSerializer


class LessonSerializer(serializers.ModelSerializer):
    # student = StudentSerializer()

    class Meta:
        model = Lesson
        fields = ["id", "description", "date", "cancelled", "student"]  # , "homework"]
        extra_kwargs = {"id": {"read_only": True}}

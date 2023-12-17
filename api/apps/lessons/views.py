from rest_framework import generics
from apps.lessons.models.lesson import Lesson
from apps.lessons.serializers.lesson_serializers import LessonSerializer
from apps.students.models import Student
from apps.lessons.permissions import IsOwnerOfLesson


class ListCreateLessonsView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsOwnerOfLesson]

    def get_queryset(self):
        return Lesson.objects.filter(student__owner=self.request.user)


class RetrieveUpdateDestroyLessonsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsOwnerOfLesson]

    def get_queryset(self):
        return Lesson.objects.filter(student__owner=self.request.user)

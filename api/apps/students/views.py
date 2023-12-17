from rest_framework import generics
from apps.students.models import Student
from apps.students.permissions import IsOwnerOfStudent
from apps.students.serializers import StudentSerializer


class ListCreateStudentsView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsOwnerOfStudent]

    def get_queryset(self):
        return Student.objects.filter(owner=self.request.user)

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx["user"] = self.request.user
        return ctx


class RetrieveUpdateDestroyStudentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsOwnerOfStudent]

    def get_queryset(self):
        return Student.objects.filter(owner=self.request.user)

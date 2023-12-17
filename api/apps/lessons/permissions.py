from rest_framework import permissions, exceptions
from apps.students.models import Student


class IsOwnerOfLesson(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        student_id = request.data.get("student", None)
        if not student_id:
            raise exceptions.ValidationError("No Student specified for lesson")
        referencing_student = Student.objects.filter(id=request.data["student"]).first()
        return (
            referencing_student is not None
            and referencing_student.owner == request.user
        )

    def has_object_permission(self, request, view, obj):
        return obj.student.owner == request.user

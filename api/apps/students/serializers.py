from rest_framework import serializers, exceptions
from apps.students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "contact_email", "image"]
        extra_kwargs = {"id": {"read_only": True}}

    def create(self, validated_data):
        user = self.context.get("user", None)
        if user is None:
            raise exceptions.ValidationError("Student without owner")
        validated_data["owner"] = user
        return super().create(validated_data)

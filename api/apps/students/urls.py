from django.urls import path
from apps.students.views import ListCreateStudentsView, RetrieveUpdateDestroyStudentView

urlpatterns = [
    path("", ListCreateStudentsView.as_view(), name="students-list-create"),
    path(
        "/<str:pk>",
        RetrieveUpdateDestroyStudentView.as_view(),
        name="students-retrieve-update-destroy",
    ),
]

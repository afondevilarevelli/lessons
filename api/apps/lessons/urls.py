from django.urls import path

from apps.lessons.views import ListCreateLessonsView, RetrieveUpdateDestroyLessonsView

urlpatterns = [
    path("", ListCreateLessonsView.as_view(), name="lessons-list-create"),
    path(
        "/<str:pk>",
        RetrieveUpdateDestroyLessonsView.as_view(),
        name="lessons-retrieve-update-destroy",
    ),
]

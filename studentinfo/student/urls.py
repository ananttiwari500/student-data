from django.urls import path
from .views import student_list, student_detail
from .apiviews import StudentList, StudentDetail

urlpatterns = [
    path("student/", StudentList.as_view(), name="student_list"),
    path("student/<int:pk>/", StudentDetail.as_view(), name="student_detail")
]

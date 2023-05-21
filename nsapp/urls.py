from django.urls import path

from nsapp.views import InstructorListView, CourseListView, InstructorDetailView, CourseDetailView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('instructors', InstructorListView.as_view()),
    path('instructors/<int:pk>', InstructorDetailView.as_view()),
    path('courses', CourseListView.as_view()),
    path('courses/<int:pk>', CourseDetailView.as_view()),
    path('auth/login', obtain_auth_token, name="create-token"),
]

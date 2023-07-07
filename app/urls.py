from django.urls import path
from .views import ResumeCreateAPIView, ResumeRUD

urlpatterns = [
    # path('', ResumeCreateAPIView),
    path('add/', ResumeCreateAPIView.as_view()),
    path('user/<int:pk>/', ResumeRUD.as_view())
]
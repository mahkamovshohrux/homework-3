from django.urls import path
from .views import CreateApiew2,ListApiView2,UpdateStatus2

urlpatterns = [
    path('create/',CreateApiew2.as_view()),
    path('all/',ListApiView2.as_view()),
    path('update/<int:pk>',UpdateStatus2.as_view())
]
from django.urls import path
from .views import ListAll,CreateAll,UpdateAll

urlpatterns=[
    path('all/',ListAll.as_view()),
    path('create/',CreateAll.as_view()),
    path('update/<int:pk>',UpdateAll.as_view())

]
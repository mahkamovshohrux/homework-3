from django.urls import path
from .views import CreateAPiView4,ListAPiView4,UpdateStatus4

urlpatterns =[
    path('create/',CreateAPiView4.as_view()),
    path('all/',ListAPiView4.as_view()),
    path('updata/<int:pk>',UpdateStatus4.as_view())

]

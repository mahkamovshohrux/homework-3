from django.urls import path
from .views import CreateAPiView5,ListAPiView5,UpdateStatus5

urlpatterns =[
    path('create/',CreateAPiView5.as_view()),
    path('all/',ListAPiView5.as_view()),
    path('updata/<int:pk>',UpdateStatus5.as_view())
]
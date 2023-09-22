from django.urls import path
from .views import CreateAPiView1,ListAPiView,UpdateStatus

urlpatterns =[
    path('create/',CreateAPiView1.as_view()),
    path('all/',ListAPiView.as_view()),
    path('updata/<int:pk>',UpdateStatus.as_view())

]

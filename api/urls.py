from django.urls import path

from . import views

app_name = 'Api'

urlpatterns = [
    path('create-user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserRetrieveView.as_view()),
    path('login/', views.SeConnecterView.as_view())
]

from . import views
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'Api'

'''
baseUrl: /api
'''

urlpatterns = [
    path('create-user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserView.as_view()),
    path('login/', views.SeConnecterView.as_view()),
    path('add-to-watchlist/', views.CreateContentView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]

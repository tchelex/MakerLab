from django.urls import path
from django.views.generic import TemplateView

from landing.views import LandingHome, RegisterationUser

urlpatterns = [
    path('', LandingHome.as_view()),
    path('registration/', RegisterationUser.as_view(), name='registration'),
]
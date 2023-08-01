from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView


# def index(request):
#     return HttpResponse("Landing")
class LandingHome(TemplateView):
    template_name = 'landing/consult-opl/index.html'


class RegisterationUser(CreateView):
    form_class = UserCreationForm
    template_name = 'landing/consult-opl/registration.html'
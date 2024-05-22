from django.shortcuts import render
from django.views.generic import TemplateView

class HomeTemp(TemplateView):
    template_name='home.html'

# Create your views here.

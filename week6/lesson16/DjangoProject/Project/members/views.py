from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import InputForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def home_view(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "home.html", context)

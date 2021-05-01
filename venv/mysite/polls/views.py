from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
# Create your views here.

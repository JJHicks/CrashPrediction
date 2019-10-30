from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Crashdata


def index(request):
    items = Crashdata.objects.all()
    template = loader.get_template('crashpredictionapp/index.html')
    context = {
        'items': items
    }
    return HttpResponse(template.render(context, request))
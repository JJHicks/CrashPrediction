from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Crashdata


def index(request):
    items = Crashdata.objects.all()
    print(len(items))
    validitems = Crashdata.objects.exclude(longitude__exact="No Data", latitude__exact="No Data")
    print(len(validitems))

    template = loader.get_template('crashpredictionapp/index.html')
    context = {
        'items': validitems
    }
    return HttpResponse(template.render(context, request))
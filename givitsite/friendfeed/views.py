from django.shortcuts import render
from django.http import HttpResponse
from .models import FoundItem

# Create your views here.

def requestItem(request):

    if request.method == 'GET':
        founditems = FoundItem.objects.all()
        return render (request, 'feed.html', {'founds':founditems})


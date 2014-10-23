# Create your views here.
from django.http.request import HttpRequest
from django.template.context import RequestContext
from django.shortcuts import render

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'establishments/home.html',
        context_instance = RequestContext(request,
        {
            'title':'Home page'
        })
    )
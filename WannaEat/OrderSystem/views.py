from django.http import HttpRequest
from django.shortcuts import render
from django.template import RequestContext

def home(request):
    """Render home page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'OrderSystem/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
        })
    )
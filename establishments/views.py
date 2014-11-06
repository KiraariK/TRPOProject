from django.http import HttpRequest
from django.shortcuts import render
from django.template import RequestContext


def cities(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'establishments/cities.html',
        context_instance=RequestContext(request,
            {
                'title': 'Home page'
            })
    )

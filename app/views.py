from django.shortcuts import render
from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('index.html', context_dict, context)
def claim(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('claim.html', context_dict, context)
def action(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('action.html', context_dict, context)
def alias(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('alias.html', context_dict, context)
def people(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('people.html', context_dict, context)

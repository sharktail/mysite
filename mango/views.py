#from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def test(req):
    latest_list = ["hello", "i", "am", "sankar."]
    template = loader.get_template('mango/index.html')
    context = RequestContext(req, {'latest_list':\
latest_list,})
    return HttpResponse(template.render(context))

def index(req):
    return HttpResponse("Hello, world.")

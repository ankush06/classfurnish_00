from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def index(request):
     return render_to_response('index.html')
     #return HttpResponse("Since you're logged in, you can see this text!")
from django.shortcuts import HttpResponse
import datetime
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def foo(request):
	return HttpResponse("Hello Python!")
def demo(request):
	return HttpResponse("testing Python!")
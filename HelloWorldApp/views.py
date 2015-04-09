from django.shortcuts import HttpResponse

# Create your views here.

def foo(request):
	return HttpResponse("Hello Python!")
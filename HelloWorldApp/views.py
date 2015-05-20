from django.shortcuts import HttpResponse
import datetime
# Create your views here.
def hello_world(request):
    return render_to_response("helloDJ/home.html",{"Testing" : "Django Template Inheritance ","HelloHello" : "Hello World - Django"})
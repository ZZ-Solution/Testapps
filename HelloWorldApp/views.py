from django.shortcuts import HttpResponse
import datetime
# Create your views here.
def index(request):
    return render_to_response("helloDJ/home.html",{"Testing" : "Django Template Inheritance ","HelloHello" : "Hello World - Django"})
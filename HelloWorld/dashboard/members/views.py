from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse("Hello world")
def method2(request):
	return HttpsResponse("This is method 2")

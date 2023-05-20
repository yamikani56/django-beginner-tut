from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello from polls view")


def details(request,question_id):
    return HttpResponse("You are looking for question with id: %s" % question_id)

def results(request,question_id):
    response="You are looking for question with id: %s"
    return HttpResponse(response % question_id)

def voting(request,question_id):
    return HttpResponse("You voted question with id: %s" % question_id)



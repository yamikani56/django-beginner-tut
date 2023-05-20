from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Question
# Create your views here.

def index(request):
    latest_question_list=Question.objects.order_by("-pub_date")[:5]
    output=", ".join([q.question_text for q in latest_question_list])
    # template = loader.get_template("polls/index.html")
    context ={
        "latest_question_list":latest_question_list
    }
    # return HttpResponse(template.render(context,request))

    return render(request,"polls/index.html",context)


def details(request,question_id):
    return HttpResponse("You are looking for question with id: %s" % question_id)

def results(request,question_id):
    response="You are looking for question with id: %s"
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You voted question with id: %s" % question_id)



from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect,HttpResponse 

from .models import Question,User
from .forms import AnswerForm,UserForm
from django.urls import reverse


def compete(request,request_id):
    context={}
    form = AnswerForm(request.POST or None)
    question=Question.objects.get(pk=request_id)
    if question:
        if question.disappear==True:
            context={
                    "output":question,
                    "form":form,
                    "answered":'answered',
                }
        else:
            context={
                    "output":question,
                    "form":form,
                }
        if int(request_id)==1:
            if question.disappear==True: 
                    context={
                    "output":question,
                    "form":form,
                    "back":'back',
                    "answered":'answered',
                    }
            else:
                    context={
                    "output":question,
                    "form":form,
                    "back":'back',
                    }
        elif int(request_id)==Question.objects.count():
            if question.disappear==True: 
                context={
                    "output":question,
                    "form":form,
                    "back":'back',
                    "answered":'answered',
                }
            else:
                context={
                    "output":question,
                    "form":form,
                    "front":'front',
                }
            
        
    return render(request,"quiz/game.html",context)

def score(request):

    user=User.objects.order_by('-id')[0]
    questions= Question.objects.all()
    for q in questions:
        q.disappear=False
        q.save()
    context={
        "user":user,
        }

    return render(request,"quiz/score.html",context)

def move(request,request_id):
    question = Question.objects.get(pk=request_id)

    user=User.objects.order_by('-id')[0]
    form=AnswerForm(request.POST or None)
    if form.is_valid():
        if question.answer==form.cleaned_data['YourAnswer']:
            question.disappear=True
            question.save()
            user.score = user.score + 10
            user.save()
    if 'submit' in request.POST:
        return HttpResponseRedirect(reverse('quiz:score')) 
    else:
        if 'next' in request.POST:
            q=int(request_id)+1                   
        elif 'previous' in request.POST:
            q=int(request_id)-1
    return HttpResponseRedirect(reverse('quiz:compete', args=(q,)))

def register(request):
  
    form=UserForm(request.POST or None )
    
    context={
            "form":form,
        }
    if form.is_valid():
        instance=form.save(commit=False)
        if  userexists(form.cleaned_data['username'],form.cleaned_data['name'])==True:
            user=User.objects.all()
            for u in user:
                if u.username==instance.username:
                    context={"user":u,}
                    return render(request,"quiz/score.html",context)
        instance.save()
        return HttpResponseRedirect(reverse('quiz:intro'))
    
    return render(request,"quiz/home.html",context)

def intro(request):
    question=Question.objects.get(pk=1)
    context={'question':question}
    form=UserForm(request.POST or None )
    user=User.objects.order_by('-id')[0]
    user.score=0
    user.save()

    questions= Question.objects.all()
    for q in questions:
        q.disappear=False
        q.save()

    context={
            'question':question,
        }
    
   
    return render(request,"quiz/intro.html",context) 

def scoreboard(request):
    user=User.objects.all()
    user=user.order_by('-score')
    context={
        'user':user,
    }

    return render(request,"quiz/scoreboard.html",context)

def userexists(user_name,full_name):
    users=User.objects.all()
    for u in users:
        if user_name==u.username:
            if full_name==u.name:
                return True
    return False
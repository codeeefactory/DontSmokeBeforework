import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
import sqlite3
#from avoidsmoke.Serializers import ContentSerializer
from .models import Content
#from rest_framework import generics
#from rest_framework.status import HTTP_204_NO_CONTENT
#from rest_framework.response import Response
from .forms import Comment, CommentForm, ContactForm, IdeaForm
# Create your views here.
db=sqlite3.connect("db.sqlite3")
cursor=db.cursor()
comments=cursor.fetchall()
def start(request):
    return render(request,"index.html")
def dontsmokered(request):
    return redirect('loading')
def dontsmokeview(request):
    ctn=Content.objects.all()
    return render(request,"home.html",{"nakesh":ctn})
def comment(request):
    context={}
    form = CommentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
           form.save()
   
    context['comment']=form
    return render(request, 'comment.html', context)
def idea(request):
    context={}
    form = IdeaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
           form.save()
   
    context['idea']=form
    return render(request, 'idea.html', context)
def Call(request):
    context={}
    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
           form.save()
   
    context['contact']=form
    return render(request, 'call.html', context)

def About(request):
	return render(request,'About.html')
# class ContentListCreate(generics.ListCreateAPIView):
#     queryset = Content.objects.all()
#     serializer_class = ContentSerializer

#     def delete(self, request, *args, **kwargs):
#         Content.objects.all().delete()
#         return Response(status=HTTP_204_NO_CONTENT)


# class ContentRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Content.objects.all()
#     serializer_class = ContentSerializer
#     lookup_field = "pk"

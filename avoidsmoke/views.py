from django.shortcuts import render
from .models import Content
# Create your views here.
def dontsmokeview(request):
    ctn=Content.objects.all()
    return render(request,"home.html",{"nakesh":ctn})
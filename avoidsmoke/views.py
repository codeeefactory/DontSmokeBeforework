from django.shortcuts import render

#from avoidsmoke.Serializers import ContentSerializer
from .models import Content
#from rest_framework import generics
#from rest_framework.status import HTTP_204_NO_CONTENT
#from rest_framework.response import Response
from .forms import Comment
# Create your views here.
def dontsmokeview(request):
    ctn=Content.objects.all()
    return render(request,"home.html",{"nakesh":ctn})
def comment(request):
    cms=Comment.objects.all()
    return render(request,"comment.html",{"comment":cms})
def Call(request):
	return render(request,'call.html')

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

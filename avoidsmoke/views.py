from django.shortcuts import render

from avoidsmoke.Serializers import ContentSerializer
from .models import Content
from rest_framework import generics
from rest_framework.status import status
from rest_framework.response import Response

# Create your views here.
def dontsmokeview(request):
    ctn=Content.objects.all()
    return render(request,"home.html",{"nakesh":ctn})
class ContentListCreate(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def delete(self, request, *args, **kwargs):
        Content.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContentRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = "pk"

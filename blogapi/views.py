from django.shortcuts import render

# Create your views here.
from blogapi.models import  posts
from rest_framework.views import APIView
from rest_framework.views import Response

class postView(APIView):
    def get(self,request,*arg,**kwargs):
        return Response(data=posts)
    def post(self,request,*args,**kwargs):
        data=request.data
        posts.append(data)
        return Response(data=data)
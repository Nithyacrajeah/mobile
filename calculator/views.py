from django.shortcuts import render

# Create your views here.
from rest_framework.views import  APIView
from rest_framework.response import Response

class AddView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2 = request.data.get("num2")
        res=n1+n2
        return Response({"msg":res})


class subView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        n1 = request.data.get("num1")
        n2 = request.data.get("num2")
        res = n1 - n2
        return Response({"msg": res})
class mulView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        n1 = request.data.get("num1")
        n2 = request.data.get("num2")
        res = n1 * n2
        return Response({"msg": res})

class facView(APIView):
    def post(self, request, *args, **kwargs):
        n1 = int(request.data.get("num1"))
        fact=1
        for i in range(1,n1+1):
            fact=fact*i
        return Response({"msg": fact})


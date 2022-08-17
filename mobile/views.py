from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from mobile.models import mobiles

# Create your views here.
#localhost:8000/api/v1/mobiles
#method get


class mobileviews(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"mobile":mobiles})

    def post(self,request,*arg,**kwargs):
        print(request.data)
        qs=request.data
        mobiles.append(qs)
        return Response({"msg":request.data})

class mobiledetailsviews(APIView):
    def get(self,request,*args,**kwargs):
        print("kwargs",kwargs)
        id=kwargs.get("id")
        qs=[mobile for mobile in mobiles if mobile.get("id")==id].pop()
        return Response({"data":qs})


from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .models import uploads
from rest_framework.views import APIView
from .serializer import registerapi,loginapi,uploads_serializer
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def home(request):
    
    return render(request,"home.html")

class register(APIView):
    def post(self,request):
        serialize=registerapi(data=request.data)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response({"msg":"sucessfull signup"})
        return Response(serialize.errors)
            
class log_in(APIView):
    def post(self, request):
        serialize=loginapi(data=request.data)
        if serialize.is_valid(raise_exception=True):
            email=serialize.data.get('email')
            password=serialize.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
               login(request,user)
               return Response({"msg":"sucessfull login"})
            else:
                return Response({"msg":"error in login"})
        return Response(serialize.errors)
            

class download(APIView):
    def get(self,request,id):
        serialize=uploads.objects.get(id=id)
        response=HttpResponse(serialize.file,content_type="application/force-download")
        response['Content-Disposition']=f'attachment:filename="{serialize.file.name}"'
        return response
       
            

class api_viewset(viewsets.ModelViewSet):
    queryset = uploads.objects.all()
    serializer_class=uploads_serializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from rest_framework import status

class HelloApiView(APIView):
    """test api view"""
    serializer_class=serializers.HelloSerializer

    def get(self ,request ,format=None):
        """returns a list of APIVIEW feature"""
        an_apiview =[
            'Uses HTTP methods as function (get , post ,put patch ,delete )',
            'It is similar to a traditional Django view ',
            'Gives you the most control over your logic',
            'It mapped manually to URLs'
        ]
        return Response({'message': 'hello' ,'an_apiview ': an_apiview})
    def post(self ,request):
        """Create a hello message with our name"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name= serializer.data.get('name')
            message= 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

        ###################################
    def put(self,request ,pk=None):
        """Handles updating an object ."""
        return Response({'method': 'put'})
##########################################
    def patch (self , request , pk=None) :
     """Patch request , only updates fields provided in the request ."""

     return Response({'method': 'patch'})
    #######################################
    def delete(self, request, pk=None):
        """Delete an object."""
        return Response({'method': 'delete'})
#######################################
def index(request):
    return render(request , 'scolarite/index.html')
##################

def inscrire(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)


        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user =authenticate(username=username , password=password)
            login(request , user)
            return redirect('index')#redirect in etudiant or enseignant
    else:
        form= UserCreationForm()

    context={'form' : form}
    return render(request, 'registration/inscrire.html', context)


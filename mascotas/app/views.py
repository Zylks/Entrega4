from email import message
from django.shortcuts import redirect, render, get_object_or_404
from app.models import Contacto
from .forms import ContactoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets,status
from .serializers import ContactoSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 



# Create your views here.
class ContactoViewset(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

@api_view(['GET', 'POST'])
def contacto_collection(request):
    if request.method == 'GET':
        contacto = Contacto.objects.all()
        serializer = ContactoSerializer(contacto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContactoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def contacto_element(request, pk):
    contacto = get_object_or_404(Contacto, id=pk)
 
    if request.method == 'GET':
        serializer = ContactoSerializer(contacto)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        contacto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        carrera_new = JSONParser().parse(request) 
        serializer = ContactoSerializer(contacto, data=carrera_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    

    
# ------------- FIN API ----------
    

def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    
    if request.method == 'POST':
        formulario =ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado"
        else:
            data["form"] = formulario
            
    return render(request, 'app/contacto.html',data)

def comida(request):
    return render(request, 'app/comida.html')

def accesorios(request):
    return render(request, 'app/accesorios.html')

def listar_contactos(request):
    contacto = Contacto.objects.all()
    
    data={
        'contacto': contacto
        
    }
    return render(request, 'app/producto/listar.html',data)

def registro(request):
    data = {
        'form': CustomUserCreationForm
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect(to="home")
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)






# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Seja bem-vindo")
    return render(request, "teste.html")

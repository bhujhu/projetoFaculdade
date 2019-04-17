from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, "index.html")

def login(request):
	return render(request, "html/login.html")

def cadastrar(request):
	return render(request, "html/cadastrar.html")

def graduacao(request):
	return render(request, "html/graduacao.html")

def posemba(request):
	return render(request, "html/posemba.html")

def tecnico(request):
	return render(request, "html/tecnico.html")
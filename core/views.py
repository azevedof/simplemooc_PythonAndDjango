from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def contact(request):
	return render(request, 'contact.html')

def contatogleison(request):
	return render(request, 'contatogleison.html')
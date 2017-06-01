from django.shortcuts import render, redirect
from .models import Book

def index(request):
	context = {
	'books':Book.objects.all()
	}
	return render(request, 'index.html', context)

def process(request):
	title = request.POST['title']
	author = request.POST['author']
	category = request.POST['category']
	Book.objects.create(title = title, author = author, category = category)	
	return redirect('/')
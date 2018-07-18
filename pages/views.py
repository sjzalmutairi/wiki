from django.shortcuts import render

# Create your views here.
from .models import Page

def list(request):
	context={
	"page": Page.objects.all(),
	}
	return render (request, 'list.html', context)

def detail(request, page_id):
	context={
	"page": Page.objects.get(id=page_id),
	}
	return render (request, 'detail.html', context)

from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.http import Http404

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .models import Category

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    all_categorys = Category.objects.all()
    context = {'all_categorys':all_categorys}
    return render(request, 'accounts/home.html', context)


def information(request, category_id):
    try:
        category  = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404('The Album does not exsit')
    return render(request,'accounts/information.html', {'category': category})

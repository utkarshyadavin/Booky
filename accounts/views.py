from django.shortcuts import render, redirect
from django.views import generic

from django.http import Http404
from django.views.generic.edit import CreateView , UpdateView , DeleteView

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Info

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    user = request.user
    context = {'user':user}
    return render(request, 'accounts/home.html' , context)



def browse(request):
    all_categorys = Category.objects.all()
    context = {'all_categorys':all_categorys}
    return render(request, 'accounts/browse.html', context)


def information(request, category_id):
    try:
        category  = Category.objects.get(pk= category_id)
    except Category.DoesNotExist:
        raise Http404('The Album does not exsit')
    return render(request,'accounts/information.html', {'category': category})


def information_added(request):

    return render(request,'accounts/redirect2.html')


def category_added(request):

    return render(request,'accounts/redirect1.html')


class CategoryCreate(CreateView):
    model = Category
    fields = ['category_name']


class InfoCreate(CreateView):
    model = Info
    fields = ['title', 'description', 'link', 'category']



def description(request, category_id, element_id):
    category = Category.objects.get(pk = category_id)
    desc = Info.objects.get(pk=element_id)
    context= {'category': category , 'desc': desc}
    return render(request,'accounts/description.html', context)





def register(request):
    if request.method=='GET':
        form = UserCreationForm()
        args = {'form': form}
        return render(request,'accounts/register.html',args)
    else:
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')




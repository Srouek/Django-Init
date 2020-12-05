from django.shortcuts import render, redirect
from .forms import ListForm
from .models import List
from django.contrib import messages 


def home(request):
    if request.method =='POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, "Item has been added to the list !")
            return render(request, "home.html", {'all_items':all_items})

        else:
            all_items = List.objects.all
            return render(request, 'index.html', {'all_items': all_items})


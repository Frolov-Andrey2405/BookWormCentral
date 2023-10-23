from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reader


def home(request):
    return render(request, 'home.html', context={"current_tab": "home"})


def readers(request):
    return render(request, 'readers.html', context={"current_tab": "readers"})


def shopping(request):
    return HttpResponse("Welcome to Shopping")


def save(request):
    name = request.POST['name']
    return render(request, 'welcome.html', context={'name': name})


def readers_tab(request):
    readers = Reader.objects.all()
    return render(request, 'readers.html', context={
        'current_tab': 'readers',
        'readers': readers
    })


def save_reader(request):
    reader_item = Reader(
        reference_id=request.POST['reader_ref_id'],
        reader_name=request.POST['reader_name'],
        reader_contact=request.POST['reader_contact'],
        reader_address=request.POST['address'],
        active=True
    )
    reader_item.save()
    return redirect('/readers')

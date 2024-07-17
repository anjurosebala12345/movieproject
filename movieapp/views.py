from django.http import HttpResponse

from movieapp.models import Movie
from django.shortcuts import render, redirect
from .forms import MovieForm

# Create your views here.

def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }

    return render(request, "index.html", context)

def detail(request, id):
    # return HttpResponse("This is movie no %s" %id)
    movie = Movie.objects.get(id=id)
    return render(request, "detail.html", {"movie": movie})

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = Movie(name=name, desc=description, year=year, image=img)
        movie.save()
    return render(request, "add.html")


def edit(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})

def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')





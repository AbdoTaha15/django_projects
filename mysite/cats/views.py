from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View

from .models import Cat, Breed

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        cl = Cat.objects.all()
        bc = Breed.objects.all().count()

        ctx = {'cat_list': cl, 'breed_count': bc}
        return render(request, 'cats/cat_list.html', ctx)
    

class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        bl = Breed.objects.all()
        ctx = {'breed_list': bl}
        return render(request, 'cats/breed_list.html', ctx)


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


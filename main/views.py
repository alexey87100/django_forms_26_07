from typing import Any, Optional
from django.db import models
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import CreateView, UpdateView

from .models import Profile, Skill
from .forms import EditCreateProfileForm, EditCreateProfileModelForm


def index(request):
    """Главная страница."""
    template = "index.html"
    profiles = Profile.objects.select_related("skill").all()
    context = {}
    context['profiles'] = profiles
    return render(request, template, context)


def profiles_by_skill(request, slug):
    """Страница с профилями с конкретным скилом."""
    skill = get_object_or_404(Skill, slug=slug)

    profiles = skill.profiles.all()

    context = {}
    context['profiles'] = profiles
    context['skill'] = skill

    return render(request, "skills.html", context)


def add_profile(request):
    """Добавление профиля сотрудника."""
    form = EditCreateProfileForm(request.POST or None)
    if form.is_valid():
        Profile.objects.create(
                        name=form.cleaned_data['name'],
                        skill=form.cleaned_data['skill'],
                        age=form.cleaned_data['age']
        )
        return redirect("/")
    return render(request, "add_profile.html", {"form": form})


def add_profile_model_form(request):
    """Добавление профиля сотрудника."""
    if request.method == 'POST':
        form = EditCreateProfileModelForm(
                                        request.POST,
                                        )
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(request, "add_profile.html", {"form": form})
    if request.method == 'GET':
        form = EditCreateProfileModelForm()
        return render(request, "add_profile.html", {"form": form})


class ProfileAddView(View):
    """Класс для создания профайла. """

    def get(self, request, *args, **kwargs):
        return render(request, 'add_profile.html', {
            'form': EditCreateProfileModelForm(),
        })

    def post(self, request, *args, **kwargs):
        form = EditCreateProfileModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return self.get(request)


class ProfileCreateView(CreateView):
    """Класс для создания профайла на основе CreateView"""
    model = Profile
    # fields = ('skill', 'name')
    form_class = EditCreateProfileModelForm
    template_name = 'add_profile.html'
    success_url = '/'


class ProfileUpdateView(UpdateView):
    """Класс для редактирования объекта модели Profile"""
    model = Profile
    context_object_name = 'profile'
    form_class = EditCreateProfileModelForm
    template_name = 'add_profile.html'
    success_url = '/'
    pk_url_kwarg = 'profile_id'

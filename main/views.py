from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from main.models import MainImage, Category


class MainView(TemplateView):
    # login_url = 'users:login'
    template_name = 'main/main.html'
    # template_name = 'main/main_t.html'
    # form_class = MainForm
    extra_context = {
        'title': 'Главная страница'
    }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['image'] = MainImage.objects.all
        context['categories'] = Category.objects.filter(archived=False)
        return context


class MainTestView(TemplateView):
    # login_url = 'users:login'
    # template_name = 'main/main.html'
    template_name = 'main/main_t.html'
    # form_class = MainForm
    extra_context = {
        'title': 'Главная страница'
    }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['image'] = MainImage.objects.all
        context['categories'] = Category.objects.filter(archived=False)
        return context


class MainMTestView(TemplateView):
    # login_url = 'users:login'
    # template_name = 'main/main.html'
    template_name = 'main/main_m.html'
    # form_class = MainForm
    extra_context = {
        'title': 'Главная страница'
    }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['image'] = MainImage.objects.all
        context['categories'] = Category.objects.filter(archived=False)
        return context
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

from main.models import MainImage, Category
from main.serializers import ListServiceSerializer
from main.services import YMLServiceXMLRenderer


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


class ListServiceAPIView(ListAPIView):
    queryset = Category.objects.filter(archived=False)
    serializer_class = ListServiceSerializer
    parser_classes = (XMLParser,)
    XMLRenderer.root_tag_name = "test"
    renderer_classes = (XMLRenderer,)

    # class CustomXMLRenderer(XMLRenderer)



class TestView(APIView):
    renderer_classes = (YMLServiceXMLRenderer,)

    def get(self, request, format=None):
        list_categorys = []
        categorys = Category.objects.filter(archived=False).all()
        for category in categorys:

            list_categorys.append(f"{category.id}: {category.name}")
        content = {'shop': {'categories': list_categorys}}
        return Response(content)


# class MainTestView(TemplateView):
#     # login_url = 'users:login'
#     # template_name = 'main/main.html'
#     template_name = 'main/main_t.html'
#     # form_class = MainForm
#     extra_context = {
#         'title': 'Главная страница'
#     }
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['image'] = MainImage.objects.all
#         context['categories'] = Category.objects.filter(archived=False)
#         return context
#
#
# class MainMTestView(TemplateView):
#     # login_url = 'users:login'
#     # template_name = 'main/main.html'
#     template_name = 'main/main_m.html'
#     # form_class = MainForm
#     extra_context = {
#         'title': 'Главная страница'
#     }
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['image'] = MainImage.objects.all
#         context['categories'] = Category.objects.filter(archived=False)
#         return context

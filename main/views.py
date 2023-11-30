from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import MainImage, Category
from main.services import YMLServiceXMLRenderer


class MainView(TemplateView):
    model = Category
    template_name = 'main/main.html'
    extra_context = {
        'title': 'Главная страница'
    }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['image'] = MainImage.objects.all
        context['categories'] = Category.objects.filter(archived=False)
        return context


class ListServiceAPIView(APIView):
    renderer_classes = (YMLServiceXMLRenderer,)

    def get(self, request, format=None):
        dict_categories = {}
        dict_services = {}
        list_services = []
        dict_shop = {
            'name': 'text_name',
            'company': 'text_company',
            'url': 'text_url',
            'platform': 'Django4.2'
        }
        categories = Category.objects.filter(archived=False).all()
        for category in categories:
            dict_categories[str(category.id)] = str(category.name)
            for service in category.service_set.filter(archived=False):
                dict_services['id'] = str(service.id)
                dict_services['name'] = str(service.name)
                dict_services['price'] = str(service.price)
                dict_services['picture'] = f'http://alfaservice.ru/{str(service.picture)}'
                dict_services['description'] = str(service.description)
                dict_services['categoryId'] = str(service.category.id)
                dict_services['currencyId'] = str(service.currencyId)
                list_services.append(dict_services)
                dict_services = {}
        dict_shop['categories'] = dict_categories
        dict_shop['offers'] = list_services
        content = {'shop': dict_shop}
        return Response(content)

from django.urls import path

from main.apps import MainConfig
from main.views import MainView, ListServiceAPIView, TestView  # , MainTestView, MainMTestView

app_name = MainConfig.name

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('service/', ListServiceAPIView.as_view(), name='service_list'),
    path('service1/', TestView.as_view(), name='service_list_test'),
    # path('test/', MainTestView.as_view(), name='main'),
    # path('m/', MainMTestView.as_view(), name='main'),
]

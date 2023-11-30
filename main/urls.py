from django.urls import path

from main.apps import MainConfig
from main.views import MainView, ListServiceAPIView

app_name = MainConfig.name

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('service/', ListServiceAPIView.as_view(), name='service_list'),
]

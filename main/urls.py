from django.urls import path

from main.apps import MainConfig
from main.views import MainView, MainTestView, MainMTestView

app_name = MainConfig.name

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('test/', MainTestView.as_view(), name='main'),
    path('m/', MainMTestView.as_view(), name='main'),
]

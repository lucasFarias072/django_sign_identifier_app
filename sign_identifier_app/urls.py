

from django.urls import path
from .views import *

urlpatterns = [
    path('', SignFormView.as_view(), name='index'),
    path('sample', SampleView.as_view(), name='sample'),
]

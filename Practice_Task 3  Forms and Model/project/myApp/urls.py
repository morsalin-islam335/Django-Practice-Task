from django.urls import path

from .views import FormAPI_RENDER, DummyForm

urlpatterns = [
    
    path("",FormAPI_RENDER, name = 'formApi'),
    path("form/", DummyForm, name = 'form page'),
]

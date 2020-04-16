from django.urls import path
from . import views

urlpatterns = [
    path('regester',views.regester,name='regester')
]
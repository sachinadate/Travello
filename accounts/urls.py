from django.urls import path
from . import views

urlpatterns = [
    path('regester',views.regester,name='regester'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]
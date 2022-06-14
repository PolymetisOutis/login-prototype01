from django.urls import path
from . import views

app_name = 'login_app'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('account/', views.account_redirect, name='account_redirect'),
    path('index_su/', views.index_su, name='index_su'),
]

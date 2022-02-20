from django.urls import path

from . import views


app_name = 'about'

urlpatterns = [
    path('about/whoami/', views.whoami),
    path('about/source_code/', views.source_code),
    path('about/random/<int:length>/<int:specials>/<int:digits>/', views.random_url)
]
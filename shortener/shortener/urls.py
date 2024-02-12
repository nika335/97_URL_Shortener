
from django.contrib import admin
from django.urls import path
from shortener_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('stats/<path:url>', views.stats, name='stats'),

]

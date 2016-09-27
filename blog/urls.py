from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^$', views.weather_chart_view, name='weather_chart_view'),
}
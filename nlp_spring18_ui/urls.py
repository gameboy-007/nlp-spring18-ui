from django.conf.urls import url
from . import views

urlpatterns = [
    # path('', views.index, name='index')
    url(r'^$', views.HomePageView.as_view(), name='home')
]
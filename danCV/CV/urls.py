from django.urls import path
from  .import views
from django.conf.urls import url
urlpatterns = [

    path('', views.home, name='home'),
    path('demo', views.demo, name='demo'),
    url(r'^view-pdf/$',views.pdf_view, name='pdf_view'),

]

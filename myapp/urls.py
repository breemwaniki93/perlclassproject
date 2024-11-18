from collections import namedtuple

from django.urls import path

from myapp import views






urlpatterns = [

    path('', views.home, name='my_home'),
    path('about_us/',views.about, name='my_about'),
    path('contact_us/',views.contact, name='my_contact'),
    path('services/', views.services, name='my_services'),
    path('blog/', views.blog, name='my_blog'),
    path('courses/', views.courses, name='my_courses'),


]
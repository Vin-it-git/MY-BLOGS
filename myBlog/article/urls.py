from django.urls import path
from article import views
urlpatterns = [
    path('',views.home,name="home"),
    path('/<int:pk>',views.blog,name='blog'),
    path('about',views.about,name='about'),

]

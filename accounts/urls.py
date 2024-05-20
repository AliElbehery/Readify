from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router= DefaultRouter()
router.register('Users', views.UserList)



urlpatterns=[
    path('signup/', views.signup),
    path('login/', views.login),
    path('',include(router.urls)),


]
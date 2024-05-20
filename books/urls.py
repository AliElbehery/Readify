from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router= DefaultRouter()
router.register('Book', views.BookViewSet)
router.register('Profile', views.ProfileViewSet)
router.register('Rating', views.RatingViewSet)
router.register('UserShelf', views.UserShelfViewSet)
router.register('Category', views.CategoryViewSet)



urlpatterns=[

    path('',include(router.urls)),

]
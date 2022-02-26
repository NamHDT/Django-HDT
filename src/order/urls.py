from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('order', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orderAPIView/', views.GetAllOrderAPIView.as_view()),
    path('listorder/', views.index, name='index'),
]
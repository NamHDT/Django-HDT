from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('order', views.OrderViewSet)
router.register('lineitemorder', views.LineItemOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orderAPIView/', views.GetAllOrderAPIView.as_view()),
    path('listorder/', views.index, name='index'),
    path('listorder1/', views.index1, name='index1'),
    path('listorder2/', views.index2, name='index2'),
]
from django.urls import path, include
from rest_framework import routers

from REST import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('router/', include(router.urls)),
    path('messages/', views.MessageListView.as_view(), name="message-list"),
    path('messages/create/', views.MessageCreateView.as_view(), name="message-create"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls

from django.urls import include, path
from rest_framework.decorators import action
from django.contrib import admin
from rest_framework import routers
from backend import views
from django.conf.urls.static import static
from django.conf import settings
# router  = routers.DefaultRouter()
# router.register(r'api/', views.DataCardViewSet, basename='card-data')

urlpatterns = [
      path('admin/', admin.site.urls),
    path('api/<str:type>/', views.DataCardApiView.as_view(), name='hello'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
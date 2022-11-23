from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from backend import views
from django.conf.urls.static import static
from django.conf import settings
router  = routers.DefaultRouter()
router.register(r'api', views.DataCardViewSet)

urlpatterns = [
      path('admin/', admin.site.urls),
    path('', include(router.urls), name='hello'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
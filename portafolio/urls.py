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
    path("chat/<str:chat_box_name>/", views.chat_box, name="chat"),
    path('api/<str:type>/', views.DataCardApiView.as_view(), name='cards'),
    path('send_email/', views.send_emails.as_view(), name='email'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
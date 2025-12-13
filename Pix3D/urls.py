from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views
from rest_framework.routers import DefaultRouter
from mainApp.views import InsumoViewSet

router = DefaultRouter()
router.register(r'insumos', InsumoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('pedido/<int:pk>/', views.realizar_pedido, name='pedido'),
    path('seguimiento/<uuid:token>/', views.seguimiento, name='seguimiento'),
    path('producto/<int:pk>/', views.detalle, name='detalle'),
    path('api/', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from emia_ecommerce.product import views 

router = DefaultRouter()
router.register(r"category", views.CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]


feat(api): configure API routes and documentation using Django Rest Framework and drf-spectacular

This commit sets up API routes for the 'Category' model using Django Rest Framework's DefaultRouter. Additionally, it integrates drf-spectacular to generate API schemas and documentation endpoints.

Summary of Changes:
- Configured a DefaultRouter for 'Category' views in the 'product' app.
- Defined API routes under '/api/' to include CRUD operations for 'Category' instances.
- Added 'SpectacularAPIView' and 'SpectacularSwaggerView' for API schema generation and interactive documentation.
- Enhanced the project's API capabilities and documentation features.

These changes improve the organization and accessibility of API endpoints while providing comprehensive documentation through drf-spectacular.

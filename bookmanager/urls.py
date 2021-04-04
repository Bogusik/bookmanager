from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from books.views import BooksViewSet
from users.views import UsersViewSet

router = routers.DefaultRouter()

router.register(r'books', BooksViewSet, basename='books')
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name='index.html'), name='index')
]

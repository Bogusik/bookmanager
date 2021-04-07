from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from django.conf import settings

from books.views import BooksViewSet
from users.views import UsersViewSet


router = routers.DefaultRouter()


router.register(r'books', BooksViewSet, basename='books')
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/auth/', obtain_jwt_token),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

paths = ['', 'login/', 'add/', 'edit/<int:pk>']
urlpatterns.extend(
    [path(x, TemplateView.as_view(template_name='index.html')) for x in paths]
)
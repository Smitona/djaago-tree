from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import SimpleRouter

from views import TreeViewSet

router = SimpleRouter()

app_name = 'tree'

router.register(
    r'tree',
    TreeViewSet,
    basename='tree'
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

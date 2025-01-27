from django.contrib import admin
from django.urls import path, include
from  rest_framework.routers import DefaultRouter
from app import views

# create router object
router = DefaultRouter()

#Register student Viewset with router
router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from .views import TodoListCreate, TodoRetrieveUpdateDestroy, login_view

schema_view = get_schema_view(
    openapi.Info(
        title="Todo list API",
        default_version='v1',
        description="APIs for keeping a track of different tasks",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="abhigyan@example.com"),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    
    path('todo/', TodoListCreate.as_view(), name= 'home'),
    path('todo/<int:pk>/', TodoRetrieveUpdateDestroy.as_view()),
    path('login/', login_view, name='login'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]

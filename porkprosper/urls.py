from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from porkprosper import views
#Api versioning
router = routers.DefaultRouter()
router.register(r'UserView', views.UserView, 'UserView')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='PorkProsper API')),
    
]

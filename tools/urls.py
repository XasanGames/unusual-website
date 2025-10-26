from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SnippetViewSet
from django.views.generic import TemplateView
from .views import snippets_page

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name="index.html")),
    path("snippets/", snippets_page, name="snippets"),
]
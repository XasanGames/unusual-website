from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tools.urls')),
     path("snippets/", TemplateView.as_view(template_name="snippets.html"), name="snippets"),
]

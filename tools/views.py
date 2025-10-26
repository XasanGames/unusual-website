# tools/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.generic import TemplateView

def index(request):
    # Отдаёт одну страницу с интерфейсом — всё на клиенте (vanilla JS)
    return render(request, "index.html")

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.order_by("-created_at")
    serializer_class = SnippetSerializer

    @action(detail=False, methods=["get"])
    def export(self, request):
        # экспорт всех сниппетов в JSON (можно доработать для скачивания)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


def snippets_page(request):
    return render(request, "snippets.html")
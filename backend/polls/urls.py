"""
Rutas URL de la app polls.
Se incluyen desde config/urls.py bajo el prefijo /api/.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Lista de todas las encuestas
    path("polls/", views.PollListView.as_view(), name="poll-list"),
    # Detalle de una encuesta por ID
    path("polls/<int:pk>/", views.PollDetailView.as_view(), name="poll-detail"),
    # Endpoint para votar
    path("vote/", views.VoteView.as_view(), name="vote"),
]

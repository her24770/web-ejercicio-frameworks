from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Poll, Option
from .serializers import PollSerializer


class PollListView(APIView):
    def get(self, request):
        polls = Poll.objects.prefetch_related("options").all()
        return Response(PollSerializer(polls, many=True).data)


class PollDetailView(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Poll.objects.prefetch_related("options"), pk=pk)
        return Response(PollSerializer(poll).data)


class VoteView(APIView):
    def post(self, request):
        option_id = request.data.get("option_id")
        if not option_id:
            return Response({"error": "Se requiere option_id"}, status=status.HTTP_400_BAD_REQUEST)

        option = get_object_or_404(Option, pk=option_id)
        Option.objects.filter(pk=option_id).update(votes=F("votes") + 1)

        poll = Poll.objects.prefetch_related("options").get(pk=option.poll_id)
        return Response(PollSerializer(poll).data)

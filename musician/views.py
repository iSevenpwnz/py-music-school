from rest_framework import viewsets
from .models import Musician
from .serializers import MusicianSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class MusicianViewSet(viewsets.ModelViewSet):

    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


@api_view(["GET", "POST"])
def manage_list(request):
    """
    List all musicians or create a new musician.
    """
    if request.method == "GET":
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = MusicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def manage_detail(request, pk):
    """
    Retrieve, update or delete a musician.
    """
    try:
        musician = Musician.objects.get(pk=pk)
    except Musician.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MusicianSerializer(musician)
        return Response(serializer.data)

    elif request.method in ["PUT", "PATCH"]:
        partial = request.method == "PATCH"
        serializer = MusicianSerializer(
            musician, data=request.data, partial=partial
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        musician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

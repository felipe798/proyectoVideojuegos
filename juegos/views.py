from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Videojuego, Genero
from .serializers import VideojuegoSerializer, GeneroSerializer
from django.http import Http404




class VideojuegoList(APIView):
    def get(self, request):
        videojuegos = Videojuego.objects.all()
        serializer = VideojuegoSerializer(videojuegos, many=True)
        return Response(serializer.data)
# Vistas para los Géneros
class GeneroList(APIView):
    def get(self, request):
        generos = Genero.objects.all()
        serializer = GeneroSerializer(generos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GeneroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GeneroDetail(APIView):
    def get_object(self, pk):
        try:
            return Genero.objects.get(pk=pk)
        except Genero.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        genero = self.get_object(pk)
        serializer = GeneroSerializer(genero)
        return Response(serializer.data)

    def put(self, request, pk):
        genero = self.get_object(pk)
        serializer = GeneroSerializer(genero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        genero = self.get_object(pk)
        genero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Vistas para los Videojuegos
class VideojuegoList(APIView):
    def get(self, request):
        videojuegos = Videojuego.objects.all()
        serializer = VideojuegoSerializer(videojuegos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideojuegoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideojuegoDetail(APIView):
    def get_object(self, pk):
        try:
            return Videojuego.objects.get(pk=pk)
        except Videojuego.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        videojuego = self.get_object(pk)
        serializer = VideojuegoSerializer(videojuego)
        return Response(serializer.data)

    def put(self, request, pk):
        videojuego = self.get_object(pk)
        serializer = VideojuegoSerializer(videojuego, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        videojuego = self.get_object(pk)
        videojuego.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

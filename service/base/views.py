from rest_framework import viewsets, status
from rest_framework.response import Response
import django_filters

from .serializers import *


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CoordsViewset(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class PerevalImagesViewset(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class LevelViewset(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class SubmitData(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalAddedSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('author__email',)
    http_method_names = ['get', 'post', 'head', 'patch', 'options']

    def create(self, request, *args, **kwargs):
        serializer = PerevalAddedSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response({f'status': status.HTTP_201_CREATED,
                             'message': 'Запись успешно создана',
                             'id': obj.id})
        if status.HTTP_400_BAD_REQUEST:
            return Response({'status': status.HTTP_400_BAD_REQUEST,
                             'message': serializer.errors})
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                             'message': serializer.errors})

    def partial_update(self, request, pk):
        pereval = Pereval.objects.get(id=pk)
        message = 'Запись успешно отредактирована'

        if 'author' in request.data:
            request.data.pop('author')
            message = ('Запись успешно отредактирована. '
                       'Замена автора не предусмотрена.')


        if pereval.status == 'NEW':
            serializer = PerevalAddedSerializer(pereval, data=request.data,
                                                 partial=True)
            if serializer.is_valid():
                obj = serializer.save()
                return Response(
                    {"state": 1,
                     "message": message,
                     'id': obj.id})
            if status.HTTP_400_BAD_REQUEST:
                return Response({"state": 0,
                                 'status': status.HTTP_400_BAD_REQUEST,
                                 'message': serializer.errors})
            if status.HTTP_500_INTERNAL_SERVER_ERROR:
                return Response({"state": 0,
                                 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                 'message': serializer.errors})
        else:
            return Response({"state": 0,
                             "message": "Запись уже рассмотрена модератором"},
                            status=400)

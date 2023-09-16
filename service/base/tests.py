import json
from rest_framework.test import APIRequestFactory, APITransactionTestCase
from django.urls import reverse
from rest_framework import status

from .models import *
from .views import SubmitData
from .serializers import PerevalAddedSerializer


class TestSimple(APITransactionTestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = SubmitData.as_view({'post': 'create',
                                        'get': 'list',
                                        'patch': 'partial_update'})
        self.my_url = '/SubmitData/'
        start_data_1 = {
                "beauty_title": "NI",
                "title": "start_title1",
                "other_titles": "start_other_title1",
                "connect": "",
                "author": {
                  "email": "abc01@yandex.ru",
                  "phone": "74951111111",
                  "fam": "Первов",
                  "name": "Один",
                  "otc": "Одинович"
                         },
                "coords": {
                  "latitude": 01.98805,
                  "longitude": 01.92527,
                  "height": 10011
                          },
                "level": {
                  "winter": "NI",
                  "summer": "NI",
                  "autumn": "NI",
                  "spring": "NI"
                        },
                "image": [
                        {
                    "image_name": "Стартовая вершина 1",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        },
                        {
                    "image_name": "Стартовая вершина 2",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        }
                        ],
                "status": "NEW",
                "spr_activities_types": "3",
               }

        start_data_2 = {
                "beauty_title": "NI",
                "title": "start_title2",
                "other_titles": "start_other_title2",
                "connect": "",
                "author": {
                  "email": "abc02@yandex.ru",
                  "phone": "749522222",
                  "fam": "Второв",
                  "name": "Два",
                  "otc": "Двович"
                         },
                "coords": {
                  "latitude": 01.98805,
                  "longitude": 01.92527,
                  "height": 10011
                          },
                "level": {
                  "winter": "NI",
                  "summer": "NI",
                  "autumn": "NI",
                  "spring": "NI"
                        },
                "image": [
                        {
                    "image_name": "Стартовая вершина 3",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        },
                        {
                    "image_name": "Стартовая вершина 4",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        }
                        ],
                "status": "NEW",
                "spr_activities_types": "3",
               }

        # start_data_1 = json.dumps(start_data_1)
        # start_data_2 = json.dumps(start_data_2)

        request_1 = self.factory.post(self.my_url,
                                      start_data_1,
                                      format='json')
        request_2 = self.factory.post(self.my_url,
                                      start_data_2,
                                      format='json')
        response_1 = self.view(request_1)
        response_2 = self.view(request_2)

        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
        self.assertEquals(Pereval.objects.count(), 2)

    def test_pereval_addition(self):
        data_1 = {
                "beauty_title": "PS",
                "title": "test_title1",
                "other_titles": "test_other_title1",
                "connect": "",
                "author": {
                  "email": "abc1@yandex.ru",
                  "phone": "74951234567",
                  "fam": "Иванов",
                  "name": "Иван",
                  "otc": "Иванович"
                         },
                "coords": {
                  "latitude": 11.988056,
                  "longitude": 11.925278,
                  "height": 11111
                          },
                "level": {
                  "winter": "NI",
                  "summer": "NI",
                  "autumn": "NI",
                  "spring": "NI"
                        },
                "image": [
                        {
                    "image_name": "Тестовая вершина 1",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        },
                        {
                    "image_name": "Тестовая вершина 2",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        }
                        ],
                "status": "NEW",
                "spr_activities_types": "1"
               }

        data_2 = {
                "beauty_title": "GL",
                "title": "test_title2",
                "other_titles": "test_other_title2",
                "connect": "",
                "author": {
                  "email": "abc1@yandex.ru",
                  "phone": "74951234567",
                  "fam": "Иванов",
                  "name": "Иван",
                  "otc": "Иванович"
                         },
                "coords": {
                  "latitude": 11.988056,
                  "longitude": 11.925278,
                  "height": 11111
                          },
                "level": {
                  "winter": "NI",
                  "summer": "NI",
                  "autumn": "NI",
                  "spring": "NI"
                        },
                "image": [
                        {
                    "image_name": "Тестовая вершина 1",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        },
                        {
                    "image_name": "Тестовая вершина 2",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        }
                        ],
                "status": "NEW",
                "spr_activities_types": "1"
               }

        request_1 = self.factory.post(self.my_url,
                                      data_1,
                                      format='json')
        response_1 = self.view(request_1)

        new_pass = Pereval.objects.last()
        self.assertEqual(new_pass.title, 'test_title1')
        self.assertEqual(new_pass.other_titles, 'test_other_title1')
        self.assertEqual(new_pass.status, 'NEW')

        request_2 = self.factory.post(self.my_url,
                                      data_2,
                                      format='json')
        # response_1 = self.view(request_1)
        response_2 = self.view(request_2)

        new_pass = Pereval.objects.last()
        self.assertEquals(Pereval.objects.count(), 4)
        self.assertEqual(new_pass.title, 'test_title2')
        self.assertEqual(new_pass.other_titles, 'test_other_title2')
        self.assertEqual(new_pass.status, 'NEW')

    def test_pereval_get_list(self):
        request = self.factory.get(self.my_url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_pereval_get_id(self):
        pereval = Pereval.objects.last()
        self.assertEquals(Pereval.objects.count(), 2)
        response = self.client.get(f'{self.my_url}{pereval.id}/')
        # response = self.view(request)
        serializer_data = PerevalAddedSerializer(pereval).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_pereval_put(self):
        pereval = Pereval.objects.last()
        self.assertEquals(Pereval.objects.count(), 2)

        data = {
                "coords": {
                  "latitude": 22.22222,
                  "longitude": 22.22222,
                  "height": 22222
                          },
                "level": {
                  "winter": "A1",
                  "summer": "А2",
                  "autumn": "B1",
                  "spring": "В2"
                        },
                }
        request = self.factory.patch(f'{self.my_url}{pereval.id}/',
                                    data,
                                   format='json')

        response = self.view(request, pk=pereval.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pereval = Pereval.objects.last()
        self.assertEqual(pereval.coords.latitude, 22.22222)
        self.assertEqual(pereval.coords.longitude, 22.22222)
        self.assertEqual(pereval.coords.height, 22222)
        self.assertEqual(pereval.level.winter, 'A1')
        self.assertEqual(pereval.level.summer, 'А2')
        self.assertEqual(pereval.level.autumn, 'B1')
        self.assertEqual(pereval.level.spring, 'В2')

    def test_unvalid_pereval_addition(self):
        data = {
                "beauty_title": "PS",
                "other_titles": "test_other_title1",
                "connect": "",
                "author": {
                  "email": "abc1@yandex.ru",
                  "phone": "74951234567",
                  "fam": "Иванов",
                  "name": "Иван",
                  "otc": "Иванович"
                         },
                "coords": {
                  "latitude": 11.988056,
                  "longitude": 11.925278,
                  "height": 11111
                          },
                "level": {
                  "winter": "NI",
                  "summer": "NI",
                  "autumn": "NI",
                  "spring": "NI"
                        },
                "image": [
                        {
                    "image_name": "Тестовая вершина 1",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        },
                        {
                    "image_name": "Тестовая вершина 2",
                    "image": "https://klike.net/uploads/posts/2022-11/1667370486_7-8.jpg"
                        }
                        ],
                "status": "NEW",
                "spr_activities_types": "1"
               }

        request = self.factory.post(self.my_url,
                                      data,
                                      format='json')
        response = self.view(request)

        self.assertEquals(Pereval.objects.count(), 2)

    def test_unvalid_pereval_put(self):
        pereval = Pereval.objects.last()
        self.assertEquals(Pereval.objects.count(), 2)
        response = self.client.get(f'{self.my_url}{pereval.id}/')

        data = {
                "author": {
                  "email": "vrong@yandex.ru",
                  "phone": "77777777",
                  "fam": "Невернов",
                  "name": "Нет",
                  "otc": "Нетолвич"
                         }
               }

        request = self.factory.patch(f'{self.my_url}{pereval.id}/',
                                    data,
                                   format='json')

        response = self.view(request, pk=pereval.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pereval = Pereval.objects.last()
        self.assertEqual(pereval.author.email, "abc02@yandex.ru")
        self.assertEqual(pereval.author.phone, "749522222")
        self.assertEqual(pereval.author.fam, "Второв")
        self.assertEqual(pereval.author.name, "Два")
        self.assertEqual(pereval.author.otc, "Двович")
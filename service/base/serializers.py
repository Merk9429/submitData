from .models import *
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['email',
                  'phone',
                  'fam',
                  'name',
                  'otc'
                  ]

    # def save(self, **kwargs):
    #     self.is_valid()
    #     current_author = Author.objects.filter(email=self.validated_data['email'])
    #     if current_author.exists():
    #         return current_author
    #     else:
    #         new_author = Author.objects.create(
    #             fam=self.validated_data.get('fam'),
    #             name=self.validated_data.get('name'),
    #             otc=self.validated_data.get('otc'),
    #             phone=self.validated_data.get('phone'),
    #             email=self.validated_data.get('email'),
    #         )
    #         return new_author


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude',
                  'longitude',
                  'height'
                  ]


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ['image_name',
                  'image'
                  ]


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter',
                  'summer',
                  'autumn',
                  'spring'
                  ]


class PerevalAddedSerializer(WritableNestedModelSerializer):
    author = AuthorSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    image = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ['beauty_title',
                  'title',
                  'other_titles',
                  'connect',
                  'author',
                  'coords',
                  'level',
                  'image',
                  'status',
                  'spr_activities_types'
                  ]

    def create(self, validated_data, **kwargs):
        author = validated_data.pop('author')
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        images = validated_data.pop('image')

        author, created = Author.objects.get_or_create(**author)

        # current_author = Author.objects.filter(email=author['email'])
        # if current_author.exists():
        #     author = current_author.first()
        # else:
        #     author = Author.objects.create(**author)

        # current_author = Author.objects.filter(email=author['email'])
        # if current_author.exists():
        #     author_serializer = AuthorSerializer(data=author)
        #     author_serializer.is_valid(raise_exception=True)
        #     author = author_serializer.save()
        # else:
        #     author = Author.objects.create(**author)

        coords = Coords.objects.create(**coords)
        level = Level.objects.create(**level)
        pereval = Pereval.objects.create(**validated_data,
                                         author=author,
                                         coords=coords,
                                         level=level
                                         )

        if images:
            for image in images:
                image_name = image.pop('image_name')
                image = image.pop('image')
                Images.objects.create(pereval=pereval,
                                      image_name=image_name,
                                      image=image)

        return pereval

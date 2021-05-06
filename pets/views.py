from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from pets.serializers import (
    CharacteristicSerializer,
    GroupSerializer,
    AnimalSerializer,
)
from pets.models import (
    Characteristic,
    Group,
    Animal,
)
import ipdb


class AnimalView(APIView):
    def post(self, request):
        serializer = AnimalSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        characteristic_set = data.pop("characteristic_set")
        group = data.pop("group")

        grp = Group.objects.get_or_create(**group)[0]

        animal = Animal.objects.create(**data, group=grp)

        for characteristic in characteristic_set:
            characteristic = Characteristic.objects.get_or_create(**characteristic)[0]

            animal.characteristic_set.add(characteristic)

        serializer = AnimalSerializer(animal)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request, animal_id=""):
        if animal_id:
            try:
                animal = Animal.objects.get(id=animal_id)
                serializer = AnimalSerializer(animal)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, animal_id):
        animal = get_object_or_404(Animal, id=animal_id)

        animal.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

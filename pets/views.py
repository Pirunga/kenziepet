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


class AnimalView(APIView):
    def post(self, request):
        serializer = AnimalSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        characteristic_set = data.pop("characteristic_set")
        group = data.pop("group")

        animal = Animal.objects.create(**data)

        all_characteristic = Characteristic.objects.all()

        for characteristic in characteristic_set:
            if characteristic not in all_characteristic:
                characteristic = Characteristic.objects.create(**characteristic)

            else:
                characteristic = Characteristic.objects.get(
                    characteristic=characteristic.name
                )

            animal.characteristics.add(characteristic)

        all_group = Group.objects.all()

        for grp in group:
            if grp not in all_group:
                grp = Group.objects.create(**grp)

            else:
                grp = Group.objects.get(name=grp.name)

            animal.group.add(grp)

        serializer = Animal(animal)

        return Response(serializer.data, status.HTTP_200_OK)

    def get(self, request, animal_id=""):
        if animal_id:
            serialized = get_object_or_404(Animal, id=animal_id)

            if not serialized.is_valid():
                return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

            try:
                animal = Animal.objects.get(id=animal_id)
                serializer = AnimalSerializer(animal)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except ObjectDoesNotExist:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, animal_id):
        serialized = get_object_or_404(Animal, id=animal_id)

        if not serialized.is_valid():
            return Response(serialized.errors, status=status.HTTP_404_NOT_FOUND)

        animal = Animal.objects.delete(id=animal_id)

        return Response(status=status.HTTP_204_NO_CONTENT)

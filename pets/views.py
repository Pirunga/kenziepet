from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pets.serializers import (
    AnimalSerializer
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
        
        data = request.data
        characteristic = data.pop('characteristics')
        group = data.pop('group')


        grp = Group.objects.get_or_create(**group)[0]

        animal = Animal.objects.create(**data, group=grp)


        # Desta forma também dá pra fazer, porém,
        # em caso de muitos dados, criar e fazer relação
        # pode acabar sendo muito demorado quando
        # feito separadamente

        # for charact in characteristic:
        #     characteristic = Characteristic.objects.get_or_create(**charact)[0]

        #     animal.characteristics.add(characteristic)


        characteristic_list = []

        for charact in characteristic:
            char = Characteristic.objects.get_or_create(**charact)[0]

            characteristic_list.append(char)

        animal.characteristics.set(characteristic_list)

        serializer = AnimalSerializer(animal)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, animal_id=""):
        if animal_id:
            animal = get_object_or_404(Animal, id=animal_id) 
            serializer = AnimalSerializer(animal)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        animal = Animal.objects.all()
        serializer = AnimalSerializer(animal, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, animal_id=''):
        animal = get_object_or_404(Animal, id=animal_id)

        animal.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

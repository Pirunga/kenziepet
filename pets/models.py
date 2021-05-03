from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name + " (" + self.scientific_name + ")"


class Characteristic(models.Model):
    characteristic = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.characteristic


class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=255)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="animals")

    characteristic_set = models.ManyToManyField(Characteristic)

    def __str__(self):
        return self.name

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here
class Pet(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pet_posts')
    pet_image = models.URLField()
    birthdate = models.DateField('Birthdate')
    gender = models.CharField(max_length=100, default='')
    spayed_or_neutered = models.CharField(max_length=100, default='')
    species = models.CharField(max_length=100, default='')
    breed = models.CharField(max_length=100, default='')
    care_notes = models.TextField(default='')
    food_notes = models.TextField(default='')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Owner(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

#class Comment(models.Model):
#    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='comments')
#    name = models.CharField(max_length=80)
#    email = models.EmailField()
#    body = models.TextField(blank=True, null=True)
#    created = models.DateTimeField(auto_now_add=True)
#    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.body}'



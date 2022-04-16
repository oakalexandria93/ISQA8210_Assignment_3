from django.contrib import admin
from .models import Pet, Owner

# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
    'name', 'owner', 'pet_image', 'birthdate','gender', 'spayed_or_neutered',
    'species', 'breed', 'care_notes', 'food_notes', 'publish')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'pet','created')
    list_filter = ('created', 'updated')
    search_fields = ('name', 'email')

#@admin.register(Comment)
#class CommentAdmin(admin.ModelAdmin):
#    list_display = ('name', 'email', 'pet', 'created')
#    list_filter = ('created', 'updated')
#    search_fields = ('name', 'email', 'body')

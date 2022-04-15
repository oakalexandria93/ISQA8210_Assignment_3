from django.shortcuts import render
from .models import *
from .forms import *

now = timezone.now()
def pet_list(request):
    object_list = Pet.objects.all().order_by('-publish')
    return render(request,'Pet/pet_list.html',
            {'pets': object_list})


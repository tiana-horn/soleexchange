from django.shortcuts import render
from core.models import Shoe

# Create your views here.
def index(request):
    shoes = Shoe.objects.all()
    return render(request, 'index.html', {
        'shoes': shoes,
    })

def shoe_detail(request, shoe_id):
    shoe = Shoe.object.get(pk=shoe_id)
    return render(request, 'shoe_deatil.html', {
        'shoe': shoe,
    })
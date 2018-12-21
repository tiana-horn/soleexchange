from django.shortcuts import render
from core.models import Shoe

# Create your views here.
def index(request):
    shoes = Shoe.objects.all()
    return render(request, 'index.html', {
        'shoes': shoes,
    })

def shoe_detail(request, slug):
    shoe = Shoe.objects.get(slug=slug)
    return render(request, 'shoe_detail.html', {
        'shoe': shoe,
    })
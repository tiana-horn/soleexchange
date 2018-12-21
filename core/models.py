from django.db import models
from django.contrib.auth.models import AbstractUser


SIZE_CHOICES = (
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    
)
# Create your models here.
class User(AbstractUser):
    pass
    

class Shoe(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    color = models.CharField(max_length=500)
    picture = models.ImageField(upload_to='shoes/', null=True)
    size = models.CharField(max_length=10, null=False, choices=SIZE_CHOICES)
    is_jordan = models.BooleanField(default=False)
    is_van = models.BooleanField(default=False)
    is_yeezy = models.BooleanField(default=False)
    is_airmax = models.BooleanField(default=False)
    is_airforce = models.BooleanField(default=False)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(default=None, unique=False)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user_cart')
    shoe = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='cart_shoe')


class Favorite(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    shoe = models.ForeignKey(to=Shoe, on_delete=models.CASCADE, related_name='favorites')

    class Meta:
        unique_together = ('shoe', 'user',)


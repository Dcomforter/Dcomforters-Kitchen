from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=15)
    email = models.EmailField(null=True)
    #phone_number = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=10, null=True)
    guest_count = models.IntegerField()
    #country = models.CharField(max_length=200)
    country = CountryField()
    comments = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)
    time = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return (
            f"{self.first_name} : "
            f"{self.last_name} : "
            f"{self.sex} : "
            f"{self.guest_count} :"
            f"{self.country}"
        )

class Menu(models.Model):
    food_name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    item_description = models.TextField(max_length=1000, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    prep_time = models.IntegerField(default=25)
    calories = models.IntegerField(default=1000)
    image = models.ImageField(upload_to='newapp/static/img/menu_items/', null=True, blank=True)
    
    def __str__(self):
        return (
            f"{self.food_name} : "
            f"{self.cuisine} : "
            f"{str(self.price)} : "
            f"{str(self.prep_time)} : "
            f"{str(self.calories)}"
        )

class Order(models.Model):
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    quantity = models.PositiveIntegerField(default=1)
    order_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.customer_name} - {self.menu_item.food_name}"
    
    @property
    def subtotal(self):
        return self.menu_item.price * self.quantity    
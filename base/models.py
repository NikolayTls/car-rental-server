from django.db import models



class Category(models.Model):
    category_name = models.CharField(max_length=100 , null = True)
    price_per_day = models.FloatField(max_length=10 , null = True)
    occupant_amount = models.CharField(max_length=100 , null = True)
    baggage_amount = models.CharField(max_length=100 , null = True)
    driver_age = models.FloatField(max_length=10 , null = True)
    Power = models.FloatField(max_length=10 , null = True)
    door_amount = models.FloatField(max_length=10 , null = True)
    acriss_code = models.CharField(max_length=100 , null = True)

    def __str__(self):
        return self.category_name

class Car(models.Model):
   
    name = models.CharField(max_length=100 , null = True)
    category = models.ForeignKey(Category , null=True, on_delete = models.SET_NULL )
    model_year = models.CharField(max_length=100 , null = True)
    description = models.CharField(max_length=100 , null = True , blank = True)
    date_created = models.DateTimeField(auto_now_add = True)
    imageUrl = models.CharField(max_length=100 , null = True)
    

    def __str__(self):
        return self.name



class City(models.Model):
    name = models.CharField(max_length=100 , null = True)

    def __str__(self):
        return self.name



class Station(models.Model):
    name = models.CharField(max_length=100 , null = True)
    street = models.CharField(max_length=100 , null = True)
    post_code = models.CharField(max_length=100 , null = True)
    image = models.ImageField(null = True , blank = True)
    phone = models.CharField(max_length=100 , null = True)
    link = models.URLField(max_length=200, blank = True)
    city = models.ForeignKey(City , on_delete = models.CASCADE)

    def __str__(self):
        return self.name 



class Reservation(models.Model):
    car = models.ForeignKey(Car , null=True, on_delete = models.SET_NULL )

    city = models.ForeignKey(City , null=True, on_delete = models.CASCADE , related_name = "pickup_city")
    station = models.ForeignKey(Station ,null=True, on_delete = models.CASCADE , related_name = "pickup_station")
    pickup_date = models.DateTimeField (null = True )
    
    

    city1 = models.ForeignKey(City ,null=True, on_delete = models.CASCADE , related_name = "return_city" )
    station1 = models.ForeignKey(Station ,null=True, on_delete = models.CASCADE , related_name = "return_station" )
    dropoff_date = models.DateTimeField (null = True )
    price = models.FloatField(max_length=10 , null = True)

 

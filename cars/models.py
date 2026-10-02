from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#MANY TO MANY
class CategoryCar(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Car(models.Model):
    title = models.CharField(max_length=100, default='BMW')
    person = models.CharField(max_length=100, default='Иванов Иван')
    categories = models.ManyToManyField(CategoryCar, null=True)

    def __str__(self):
        return f'{self.title}Категории: {', '.join(i.name for i in self.categories.all())}'

# one to one

class StateNumberCar(models.Model):
    car_title = models.OneToOneField(Car, on_delete=models.CASCADE)
    number_car = models.CharField(max_length=100, default="0_KG______")

    def __str__(self):
        return f'{self.car_title}-{self.number_car}'


# one to Many
class CommentCar(models.Model):
    choice_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), 
                                                              MaxValueValidator(5)])
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_car}-{self.mark}'
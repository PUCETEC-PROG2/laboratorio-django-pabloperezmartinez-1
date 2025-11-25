from django.db import models
from django.utils import timezone

class Trainer(models.Model):
    name = models.CharField(max_length=100, null=False)
    birth_date = models.DateField(null=False)
    level = models.IntegerField(null=False)
    picture = models.ImageField(upload_to='trainers/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    @property
    def age(self):
        today = timezone.now().date()
        age = today.year - self.birth_date.year
        # Adjust age if the birthday hasn't occurred yet this year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

class Pokemon(models.Model):
    name = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=40, null=False)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    picture = models.ImageField(upload_to='pokemons/', null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name
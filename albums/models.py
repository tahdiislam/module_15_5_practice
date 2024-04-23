from django.db import models
from musicians.models import Musician


# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    CHOICES_OF_RATING = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")]
    rating = models.CharField(choices=CHOICES_OF_RATING, max_length=5)

    def __str__(self) -> str:
        return f"Name: {self.name}"
from django.conf import settings
from django.db import models

class Experience(models.Model):
    name = models.CharField(max_length=30)
    points = models.DecimalField(max_digits=100, decimal_places=2)

    def status(self):
        if self.points <= 10:
            return 'Командир взвода'
        elif self.points > 10 and self.points <= 20:
            return 'Командир роты'
        elif self.points > 20 and self.points <= 35:
            return 'Командир батальона'
        elif self.points > 35:
            return 'Командир полка'

    def __str__(self):
        return self.name

class Rank(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='new_war_time/static/img/rank_images/')
    points = models.DecimalField(max_digits=100, decimal_places=1)

    def __str__(self):
        return self.name

class Combat_squad(models.Model):
    number_of_persons = models.DecimalField(max_digits=10000, decimal_places=0)

class User(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    full_name = models.CharField(max_length=30)
    experience= models.ForeignKey(Experience, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    combat_squad = models.ForeignKey(Combat_squad, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

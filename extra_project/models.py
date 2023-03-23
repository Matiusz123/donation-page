from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Institution(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    type_choices = (
        ('a', 'fundacja'),
        ('b', 'organizacja pozarządowa'),
        ('c', 'zbiórka lokalna'),
        ('d', 'domyślnie fundacja'),

    )
    type = models.CharField(max_length=1, choices=type_choices)
    models.ManyToManyField(Category, through='CategoriesInst')

    class Meta:
        verbose_name_plural = "Institutions"

    def __str__(self):
        return f"{self.name} opis = {self.description} "


class Donation(models.Model):
    quantity = models.IntegerField()
    models.ManyToManyField(Category, through='CategoriesDonation')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    pick_up_date = models.DateField(auto_now=True)
    pick_up_time = models.DateField(auto_now=True)
    pick_up_comment = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=0)


class CategoriesDonation(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)


class CategoriesInst(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
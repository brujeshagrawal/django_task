from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class User(models.Model):
    GENDERS = [
        ('M', 'Male'),
        ('F','Female'),
    ]
    phone_regex = RegexValidator(regex = r'^(\+\d{1,3}[- ]?)?\d{10}$', message="Indian mobile number")

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_number = models.CharField(validators=[phone_regex], max_length=15)
    email = models.EmailField(primary_key = True)
    gender = models.CharField(max_length=1, choices = GENDERS,)
    dob = models.DateField()
    created_date = models.DateTimeField(auto_now_add = True)
    Password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

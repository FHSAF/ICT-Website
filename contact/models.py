from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator

class Contact(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone_regex = RegexValidator(
      regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
  phone_number = models.CharField(
      validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
  birth_date = models.DateField()
  subject = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.name

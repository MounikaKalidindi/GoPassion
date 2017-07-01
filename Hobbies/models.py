from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model) :
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	intrest = models.CharField(max_length=30)
	name = models.CharField(max_length=30)
@receiver (post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created :
		Profile.objects.create(user=instance)
@receiver (post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

class Categories(models.Model):
	category = models.CharField(max_length=50)
	def __str__(self):
		return self.category


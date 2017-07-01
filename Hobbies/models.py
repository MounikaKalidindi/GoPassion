from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model) :
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	intrest = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
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

class Sub_Categories(models.Model):
	sub_category = models.CharField(max_length=50)
	def __str__(self):
                return self.sub_category

class Categories_Sub_Categories_Mapping(models.Model):
	category_id = models.ForeignKey(Categories)
	sub_category_id = models.ForeignKey(Sub_Categories)
	def __str__(self):
		return "{0}-{1}".format(self.category_id, self.sub_category_id)

class Sub_Categories1(models.Model):
	sub_category = models.ForeignKey(Sub_Categories)
	sub_category1 = models.CharField(max_length=50)
	def __str__(self):
		return "{0}-{1}".format(self.sub_category, self.sub_category1)

class Sub_Categories_Sub_Categories1_Mapping(models.Model):
	sub_category = models.ForeignKey(Sub_Categories)
	sub_category1 = models.ForeignKey(Sub_Categories1)
	def __str__(self):
		return "{0}-{1}".format(self.sub_category, self.sub_category1)

class Details(models.Model):
	sub_category1_map_id = models.ForeignKey(Sub_Categories_Sub_Categories1_Mapping)
	description = models.CharField(max_length=500)
	video = models.CharField(max_length=300)
	image = models.CharField(max_length=300)
	def __str__(self):
		return "{0}-{1}-{2}-{3}".format(self.sub_category1_map_id, self.description, self.video, self.image)

class FeedBack(models.Model):
	feedback = models.CharField(max_length=50)
	suggesions = models.CharField(max_length=50)
	category_id = models.ForeignKey(Categories)
	def __str__(self):
		return "{0}-{1}-{2}".format(self.feedback, self.suggesions, self.category_id)

class Posts(models.Model):
	category_id = models.CharField(max_length=50)
	post_adv = models.BooleanField()
	img = models.CharField(max_length=300)
	video = models.CharField(max_length=300)
	description = models.CharField(max_length=300)
	def __str__(self):
		return "{0}-{1}-{2}-{3}-{4}".format(self.category_id, self.post_adv, self.img, self.video, self.description)

class Utilities(models.Model):
	utility = models.CharField(max_length=50)
	links = models.CharField(max_length=50)
	def __str__(self):
		return "{0}-{1}".format(self.utility, self.links)

class Details_Utilities_Mapping(models.Model):
	details_id = models.ForeignKey(Details)
	utility_id = models.ForeignKey(Utilities)
	def __str__(self):
		return "{0}-{1}".format(self.details_id, self.utility_id)

"""class Followers(models.Model):
	user = models.ForeignKey(User)
	follow = models.ForeignKey(User)
	def __str__(self):
		return "{0}-{1}".format(self.user_id, self.follower_id)"""

class ScoreBoard(models.Model):
	category_id = models.ForeignKey(Categories)
	rank = models.IntegerField()
	user_name = models.ForeignKey(Profile)
	def __str__(self):
		return "{0}-{1}-{2}".format(self.category_id, self.rank, self.user_name)

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    intrest = models.CharField(max_length=50)
    name = models.CharField(max_length=50)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Categories(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Sub_Categories(models.Model):
    sub_category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_category_name


class Categories_Sub_Categories_Mapping(models.Model):
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(Sub_Categories, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}-{1}".format(self.category_id, self.sub_category_id)


class Sub_Categories1(models.Model):
    # sub_category = models.ForeignKey(Categories_Sub_Categories_Mapping, on_delete = models.CASCADE)
    sub_category1_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_category1_name


class Sub_Categories_Sub_Categories1_Mapping(models.Model):
    sub_category_id = models.ForeignKey(Sub_Categories, on_delete=models.CASCADE)
    sub_category1_id = models.ForeignKey(Sub_Categories1, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}-{1}".format(self.sub_category_id, self.sub_category1_id)


class Tutorials(models.Model):
    sub_category1_map_id = models.ForeignKey(Sub_Categories_Sub_Categories1_Mapping, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    video = models.CharField(max_length=300)
    image = models.CharField(max_length=300)

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.sub_category1_map_id, self.description, self.video, self.image)


class FeedBack(models.Model):
    feedback = models.CharField(max_length=50)
    suggesions = models.CharField(max_length=50)
    category_map_id = models.ForeignKey(Categories_Sub_Categories_Mapping, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.feedback, self.suggesions, self.category_id)


class Posts(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_map_id = models.ForeignKey(Categories_Sub_Categories_Mapping, on_delete=models.CASCADE)
    post_adv = models.BooleanField()
    src = models.FileField(max_length=300)
    likes = models.IntegerField()
    description = models.CharField(max_length=300)

    def __str__(self):
        return "{0}-{1}-{2}-{3}-{4}-{5}".format(self.user_id, self.category_map_id.id, self.post_adv, self.src,
                                                self.likes, self.description)


class Advertisements(models.Model):
    user_id = models.ForeignKey(User)
    category_map_id = models.ForeignKey(Categories_Sub_Categories_Mapping, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.user_id, self.category_id, self.post_id)


"""
class Utilities(models.Model):
	utility = models.CharField(max_length=50)
	links = models.CharField(max_length=50)
	def __str__(self):
		return "{0}-{1}".format(self.utility, self.links)

class Details_Utilities_Mapping(models.Model):
	details_id = models.ForeignKey(Details, on_delete = models.CASCADE)
	utility_id = models.ForeignKey(Utilities, on_delete = models.CASCADE)
	def __str__(self):
		return "{0}-{1}".format(self.details_id, self.utility_id)
"""


class Followers(models.Model):
    user_id = models.ForeignKey(User, related_name="user_id", on_delete=models.CASCADE)
    follower_id = models.ForeignKey(User, related_name="follower_id", on_delete=models.CASCADE)

    def __str__(self):
        return "{0}-{1}".format(self.user_id, self.follower_id)


class ScoreBoard(models.Model):
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    rank = models.IntegerField()
    user_name = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.category_id, self.rank, self.user_name)

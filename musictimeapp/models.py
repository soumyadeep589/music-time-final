from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from hashlib import md5
from django import template
from django.db.models import Count
from django.urls import reverse




class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    avatar = models.ImageField(upload_to='avatars/')


    def avatarr(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    # def follow(self, user):
    #     if not self.is_following(user):
    #         self.follows.append(user)

    # def unfollow(self, user):
    #     if self.is_following(user):
    #         self.follows.remove(user)

    # def is_following(self, user):
    #     return self.follows.filter(Follow.following == user).count() > 0

    # def followed_posts(self):
    #     followed = Post.query.join(
    #         Follow, (Follow.following == Post.author)).filter(
    #             Follow.following == self)
    #     own = Post.query.filter_by(user_id=self)
    #     return followed.union(own).order_by(Post.timestamp.desc())



    REQUIRED_FIELDS = ['avatar', ]

    def __str__(self):
        return self.email


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE
    )


class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="who_follows", on_delete=models.CASCADE)
    followed = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,related_name="who_is_followed", on_delete=models.CASCADE)
    follow_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.follow_time)

    def is_following(self, current_user, user):
        return self.objects.filter(follower=current_user, followed=user).annotate(count=Count('follower')).length > 0


STUDIOTYPE_CHOICES = [
    ('rehearsal_space', 'Rehearsal Space'),
    ('podcast_space', 'Podcast Space'),
    ('home_studio', 'Home Studio'),
    ('mid_level_studio', 'Mid-Level-Studio'),
    ('top_line_studio', 'Top-Line-Studio')
]


class Studio(models.Model):
    id = models.AutoField(primary_key=True)
    studio_name = models.CharField(max_length=40, blank=False)
    studio_details = models.TextField(blank=False)
    studio_type = models.CharField(max_length=20, choices=STUDIOTYPE_CHOICES, default='rehearsal_space')
    past_clients = models.CharField(max_length=200, null=True, blank=True)
    audio_samples = models.CharField(max_length=200, null=True, blank=True)
    equipments = models.CharField(max_length=300, null=True, blank=True)
    address = models.CharField(max_length=200, blank=False)
    price_per_hour = models.FloatField(blank=False)
    studio_image = models.ImageField(upload_to='studio_images/')
    studio_owner = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        return reverse('studios')

    def __str__(self):
        return self.studio_name

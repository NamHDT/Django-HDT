from django.db import models
from django.contrib.auth.models import AbstractUser, Group, User
# Create your models here.

class Team(models.Model):
    title_team = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title_team

class Group(models.Model):
    title_group = models.CharField(max_length=255)


    def __str__(self):
        return self.title_team

class Accounts(models.Model):
    accounts_fullname = models.CharField(max_length=200)
    user = models.OneToOneField(User,related_name='accounts', on_delete=models.CASCADE)
    accounts_key = models.CharField(max_length=50, unique=True)
    birthday = models.DateField(null=True, blank=True)
    key_vendor = models.CharField(max_length=100, default=None, null=True, blank=True)
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=12, default=None, null=True, blank=True)
    address = models.CharField(max_length=100, default=None, null=True, blank=True)
    mail = models.CharField(max_length=100, default=None, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    link_image_facebook = models.CharField(max_length=100, default=None, null=True, blank=True)
    link_telegram = models.CharField(max_length=100, default=None, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.accounts_fullname
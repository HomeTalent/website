# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Mail(models.Model):

    USER_TYPES = (
        ('A', 'ASKER'),
        ('T', 'TASKER')
    )
    
    address = models.EmailField()
    user_type = models.CharField(
        max_length=1,
        choices=USER_TYPES,
        default='A'
    )
    service = models.CharField(
        max_length=400
    )
    created_date = models.DateTimeField(
        default=timezone.now
    )

    def publish(self):
        self.save()

    def __str__(self):
        return self.address

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from accounts.models import User

@python_2_unicode_compatible
class Question(models.Model):
    # pass
    user = models.ForeignKey(User,blank=True, null=True)
    question_text = models.CharField(max_length=200, default="")
    pub_date = models.DateTimeField(
        blank=True, 
        null=True,
        auto_now_add=True
        )

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return '{} by {}'.format(self.user, self.question_text)

class Choice(models.Model):
    # pass
    question = models.ForeignKey(Question, 
                        on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible
# from accounts.models import User
from django.contrib.auth.models import User

CHOICE_ORDER_OPTIONS = (
    ('content',_('Content')),
    ('random',_('Random')),
    ('none',_('None'))
)

@python_2_unicode_compatible
class Question(models.Model):
    user = models.ForeignKey(User,blank=True, null=True)
    question_text = models.CharField(
        max_length=200, default="",
    )
    pub_date = models.DateTimeField(
        blank=True, 
        null=True,
        auto_now_add=True
        )
    choice_order = models.CharField(
        max_length=30, 
        null=True, 
        blank=True,
        choices = CHOICE_ORDER_OPTIONS,
        help_text=_("The order in which choices are"
                    " displayed to the user."),
        verbose_name=_("Choice Order")
    )

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def order_choices(self, queryset):
        if self.choice_order == 'content':
            return queryset.order_by('content')
        if self.choice_order == 'random':
            return queryset.order_by('?')
        if self.choice_order == 'none':
            return queryset.order_by()
        return queryset

    def get_choices(self):
        return self.order_choices(Choice.objects.filter(question=self))

    def get_choices_list(self):
        return [(choice.id, choice.choice_text)for choice in self \
                .order_choices(Choice.objects.filter(question=self))]

    def choice_to_string(self, guess):
        return Choice.objects.get(id=guess).choice_text

    def __str__(self):
        return '{} by {}'.format(self.question_text, self.user)


class Choice(models.Model):
    # pass
    question = models.ForeignKey(Question, 
                        on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


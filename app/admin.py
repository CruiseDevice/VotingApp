# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]

    list_display = ('question_text', 'user', 'pub_date')
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)

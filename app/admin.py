# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)
from django.contrib import admin

from .models import Candidate, UserProfile, Choice

admin.site.register(Candidate)
admin.site.register(Choice)
admin.site.register(UserProfile)

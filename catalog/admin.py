from django.contrib import admin

# Register your models here.
from .models import Lesson, Tag, Topic
admin.site.register(Lesson)
admin.site.register(Tag)
admin.site.register(Topic)
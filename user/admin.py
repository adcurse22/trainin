from django.contrib import admin
from .models import Category,Exercise,Nutrition,Feedback
admin.site.register(Category)
admin.site.register(Exercise)
admin.site.register(Nutrition)
admin.site.register(Feedback)
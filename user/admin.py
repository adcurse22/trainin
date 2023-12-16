
from .models import Category,Exercise,Nutrition,Feedback,UserManager
from django.contrib import admin
from .models import Nutrition
admin.site.register(Category)
admin.site.register(Exercise)
admin.site.register(Feedback)

@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'description', 'photo')
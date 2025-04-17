from django.contrib import admin
from .models import User, Skill, Product, Work

admin.site.register(User)
admin.site.register(Skill)
admin.site.register(Product)
admin.site.register(Work)

# Register your models here.

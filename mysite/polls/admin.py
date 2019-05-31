from django.contrib import admin
from .models import Question
# Register your models here.

# tell admin that questin objects have an admin interface
admin.site.register(Question)
from django.contrib import admin
from .models import Book,Contact,News,Post,Profile
# Register your models here.
admin.site.register(Book)
admin.site.register(Contact)
admin.site.register(News)
admin.site.register(Post)
admin.site.register(Profile)
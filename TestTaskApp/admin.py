from django.contrib import admin

from TestTaskApp.models import Autors, Books,User

admin.site.register(Books)
admin.site.register(Autors)
admin.site.register(User)

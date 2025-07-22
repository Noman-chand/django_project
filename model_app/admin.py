from django.contrib import admin
from model_app.models import Person
# Register your models here.

admin.site.register(Person)


# if we want to display data like database table then we make class for this and register with
# second parameter in register
#syntax
# class PersonAdmin(admin.ModelAdmin):
#     list_data = ['first_name', 'last_name']
#
# admin.site.register(Person, PersonAdmin)

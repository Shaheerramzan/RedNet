from django.contrib import admin

# Register your models here.
from Person.models import Person, Phone


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'gender', 'blood_group', 'phone')
    search_fields = ('first_name',)
    list_filter = ('blood_group',)


@admin.register(Phone)
class PersonAdmin(admin.ModelAdmin):
    pass

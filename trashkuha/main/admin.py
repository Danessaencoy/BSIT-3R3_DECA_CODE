from django.contrib import admin
from .models import booking
# Register your models here.

@admin.register(booking)
class bookingAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'address', 'collection_date', 'approved')
	ordering = ('collection_date',)
	search_fields = ('name', 'address')
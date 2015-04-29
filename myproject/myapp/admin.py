from django.contrib import admin
from myapp.models import Program
from myapp.models import Session
from myapp.models import Location
from myapp.models import Customer
from myapp.models import Image

class ProgramAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ['title', 'priority', 'status', 'create_date', 'modify_date']
    ordering = ['priority', 'title']
    actions = ['publish_programs']

def publish_programs(self, request, queryset):
	rows_updated = queryset.update(status='p')
	if rows_updated == 1:
		message_bit = "1 program was"
	else:
		message_bit = "%s programs were" % rows_updated
	self.message_user(request, "%s successfully marked as published." % message_bit)

class SessionAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'location', 'start_date', 'create_date', 'modify_date']
    ordering = ['title']
    actions = ['publish_sessions']
    save_as = True

def publish_sessions(self, request, queryset):
	rows_updated = queryset.update(status='p')
	if rows_updated == 1:
		message_bit = "1 session was"
	else:
		message_bit = "%s sessions were" % rows_updated
	self.message_user(request, "%s successfully marked as published." % message_bit)

class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    ordering = ['name']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['firstname']

class PictureAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']

admin.site.register(Program, ProgramAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Image, PictureAdmin)

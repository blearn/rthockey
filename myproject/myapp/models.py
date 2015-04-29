import datetime
import os

from django.db import models
from django.utils import timezone

from django.conf import settings

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)

imgtag = "<img border='0' alt='' src='%s' />"

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Program(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    create_date = models.DateTimeField(editable=False)
    modify_date = models.DateTimeField(editable=False)
    priority = models.IntegerField()
    cost = models.IntegerField()
    location = models.ForeignKey(Location)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

	def is_new(self):
		return self.create_date >= timezone.now() - datetime.timedelta(days=7)

    def save(self, *args, **kwargs):
        ''' on save, update timestamps '''
        if not self.id:
            self.create_date = timezone.now()
        self.modify_date = timezone.now()
        return super(Program, self).save(*args, **kwargs)

    def getUrl(self, obj):
        return '/register/program/%s' % ( obj.id )

class Session(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    agegroup = models.CharField(max_length=100)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    cost = models.IntegerField()
    program = models.ForeignKey(Program)
    location = models.ForeignKey(Location)
    create_date = models.DateTimeField(editable=False)
    modify_date = models.DateTimeField(editable=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    def save(self, *args, **kwargs):
        ''' on save, update timestamps '''
        if not self.id:
            self.create_date = timezone.now()
        self.modify_date = timezone.now()
        return super(Session, self).save(*args, **kwargs)

class Customer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birthdate = models.DateField()
    address = models.CharField(max_length=1000)
    parent_guardian_name = models.CharField(max_length=200)
    home_phone = models.CharField(max_length=15)
    email = models.CharField(max_length=250)
    emergency_contact = models.CharField(max_length=1000)
    medical_conditions = models.CharField(max_length=65535)
    height_inches = models.CharField(max_length=2)
    weight_pounds = models.CharField(max_length=3)
    is_locked = models.BooleanField(default=True)
    other_phones = models.CharField(max_length=1000)
    create_date = models.DateTimeField(editable=False, default=timezone.now())
    modify_date = models.DateTimeField(editable=False, default=timezone.now())
    
    def save(self, *args, **kwargs):
        ''' on save, update timestamp '''
        if not self.id:
            self.create_date = timezone.now()
        self.modify_date = timezone.now()
        return super(Customer, self).save(*args, **kwargs)

class Image(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=65535)

    def __unicode__(self):
        return self.image.name

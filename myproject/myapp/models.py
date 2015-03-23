import datetime

from django.db import models
from django.utils import timezone

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)

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

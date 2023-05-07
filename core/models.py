from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from autoslug import AutoSlugField
User = get_user_model()

CHOICES = (
     ('yes', 'yes'),
     ('no', 'no')
)
CATEGORIES = (
     ('earth','earth'),
     ('business', 'business'),
     ('health', 'health'),
     ('technology', 'technology'),
     ('law', 'law'),
     ('marine', 'marine'),
     ('nationalism', 'nationalism'),

)


class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id_user = models.IntegerField(null=True)
    nationality = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    about_me = models.CharField(max_length=200)
    date_joined = models.DateField(auto_now_add=True)    
    
    def __str__(self):
        return self.owner.username

class Course(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from="title", unique=True)
    featured_image = models.ImageField(upload_to="Course Images")
    author = models.CharField(max_length=100)
    number_of_lectures = models.CharField(max_length=300)
    category = models.CharField(max_length=300, choices=CATEGORIES)
    description = models.TextField()

    def __str__(self):
        return self.title

class Lecture(models.Model):
    title = models.CharField(max_length=300)
    video_link = models.CharField(max_length=900)
    description = models.TextField()
    serial_number = models.IntegerField()
    course = models.ForeignKey(Course, on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return self.title

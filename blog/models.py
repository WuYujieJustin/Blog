from django.db import models
from django.utils import timezone
# Create your models here.

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.ForeignKey('Tag', on_delete=models.SET_NULL, null=True)
    # one tag can have many books while one book can only have one tag
    userid = models.CharField(max_length= 10, default = 'Justin')
    title = models.CharField(max_length = 100)
    listimage = models.ImageField(null = True, blank=True, upload_to = "media", width_field="width_field", height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    blogimage = models.ImageField(null = True, blank=True, upload_to = "media", width_field="width_field", height_field="height_field")
    summary = models.CharField(max_length = 200)
    created = models.DateField(null = True, blank=True)
    heading1 = models.CharField(max_length = 100,blank=True, default = 'Justin')
    pra1 = models.TextField(max_length = 2000,blank=True, default = 'Justin')
    heading2 = models.CharField(max_length = 100,blank=True, default = 'Justin')
    pra2 = models.TextField(max_length = 2000,blank=True, default = 'Justin')
    heading3 = models.CharField(max_length = 100,blank=True, default = 'Justin')
    pra3 = models.TextField(max_length = 2000,blank=True, default = 'Justin')
    heading4 = models.CharField(max_length = 100,blank=True, default = 'Justin')
    pra4 = models.TextField(max_length = 2000,blank=True, default = 'Justin')

    class meta:
        ordering = ["-created"]
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.summary

    def get_absolute_url(self):
        """
        Returns the url to access a particular
        """
        return reverse('blog-detail', args=[str(self.id)])

    def getpreviouse_post(self):

        return reverse('blog-detail', args=[str(self.id-1)])

    def getlater_post(self):

        return reverse('blog-detail', args=[str(self.id+1)])




class Tag(models.Model):
    """
    Model representing a blog type (e.g.blog diary).
    """
    BLOG_TYPE = (
        ('Blog', 'Blog'),
        ('Daily Life', 'Daily Life'),
        ('Work', 'Work'),
        ('Study', 'Study'),
    )
    
    type = models.CharField(max_length=10, choices=BLOG_TYPE, blank=True, default='m', help_text='blog type')

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.type

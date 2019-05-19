from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        try:
            return str(self.image.url.split('\\')[-1])
        except Exception as e:
            return None
        else:
            return str(self.image.url.split('/')[-1])
        finally:
            return self.image.url


class About(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300)
    DOB = models.DateField()
    about = models.TextField()
    cv = models.FileField(max_length=320)
    skills = models.ManyToManyField('Skill')
    github = models.URLField(max_length=200, null=True)
    facebook = models.URLField(max_length=200, null=True)
    linkedin = models.URLField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = "About"


class Experience(models.Model):
    employer_name = models.CharField(max_length=128)
    job_title = models.CharField(max_length=128)
    Description = RichTextUploadingField()
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)
    to_display = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Experience"
        ordering = ['-from_date', '-to_date']


class Education(models.Model):
    college = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)
    description = RichTextUploadingField()
    to_display = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Education"
        ordering = ['-to_date', '-from_date']


class Project(models.Model):
    name = models.CharField(max_length=128)
    priority = models.IntegerField()
    content = models.TextField()
    image = models.ForeignKey(
        Image, null=True, on_delete=models.CASCADE)
    to_display = models.BooleanField(default=True)
    link = models.URLField(max_length=320, null=True)

    class Meta:
        verbose_name_plural = 'Projects'
        ordering = ['priority']


class Skill(models.Model):
    name = models.CharField(max_length=30)
    to_display = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)

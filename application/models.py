from django.db import models
from django.utils.text import slugify

class Student(models.Model):
    name = models.CharField(max_length=100,blank=False)
    surname = models.CharField(max_length=100,blank=False)
    age = models.PositiveIntegerField(default=30,blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='students/',default='students/default.jpg',blank=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *islombek, **alyosha):
        if not self.slug:
            self.slug = slugify({self.name}-{self.surname})
        super().save(*islombek, **alyosha)

    def __str__(self):
        return f"{self.name} {self.surname}"
from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Message = models.TextField()
    Date = models.DateField()
    timeStamp = models.CharField(max_length=200)

class Campaign(models.Model):
    Title = models.CharField(max_length= 200)
    Description = models.TextField()
    MinimumAmount = models.IntegerField(blank=True)
    Image= models.FileField(upload_to='files', blank=True)

class HomeSlider(models.Model):
    Image= models.FileField(upload_to='files', blank=False)
    Description = models.CharField(max_length=100, blank=True)

    def delete(self, *args, **kwargs):
        self.Image.delete()
        super().delete(*args, **kwargs)
from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Message = models.TextField()
    Date = models.DateField()
    timeStamp = models.CharField(max_length=200)

class HomeSlider(models.Model):
    Image= models.ImageField(upload_to='files', blank=False)
    Description = models.CharField(max_length=100)

    def delete(self, *args, **kwargs):
        self.Image.delete()
        super().delete(*args, **kwargs)
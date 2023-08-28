from django.db import models

class Blog(models.Model):
    article_title= models.CharField(max_length=100, null=False, default="Heading")
    article = models.TextField()
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.article_title} - Article'
    
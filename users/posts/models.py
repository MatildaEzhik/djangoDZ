from django.db import models

# Create your models here.


from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

